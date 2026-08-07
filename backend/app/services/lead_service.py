from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.ai.qualification import LeadQualification
from app.ai.communication import AICommunication
from app.ai.appointment_recommendation import AppointmentRecommendation

from app.repositories.lead_repository import LeadRepository
from app.repositories.activity_repository import ActivityRepository
from app.repositories.appointment_repository import AppointmentRepository
from app.repositories.conversation_repository import ConversationRepository
from app.repositories.follow_up_repository import FollowUpRepository

from app.schemas.lead import LeadCreate, LeadUpdate

from app.services.activity_service import ActivityService
from app.services.google_sheet_service import GoogleSheetService
from app.services.automation_service import AutomationService


class LeadService:

    @staticmethod
    def create_lead(db: Session, lead: LeadCreate):

        print("\n================ CREATE LEAD =================")

        # ==========================================
        # Duplicate Validation
        # ==========================================

        print("Checking duplicate email...")

        if LeadRepository.get_by_email(db, lead.email):
            raise HTTPException(
                status_code=400,
                detail="Lead already exists with this email."
            )

        print("Checking duplicate phone...")

        if LeadRepository.get_by_phone(db, lead.phone):
            raise HTTPException(
                status_code=400,
                detail="Lead already exists with this phone number."
            )

        # ==========================================
        # AI Qualification
        # ==========================================

        print("Running AI Qualification...")

        try:

            result = LeadQualification.qualify(
                {
                    "budget": lead.budget,
                    "timeline": lead.purchase_timeline,
                    "vehicle": lead.vehicle_interest,
                    "city": lead.city,
                }
            )

            print("AI Response:")
            print(result)

            # ==========================================
            # AI Communication
            # ==========================================

            print("Generating AI Communication...")

            communication = AICommunication.generate(
                {
                    "full_name": lead.full_name,
                    "vehicle_interest": lead.vehicle_interest,
                    "budget": lead.budget,
                    "purchase_timeline": lead.purchase_timeline,
                    "city": lead.city,
                    "qualification_status": result["qualification_status"],
                    "priority": result["priority"],
                    "recommended_action": result["recommended_action"]
                }
            )

            print("AI Communication:")
            print(communication)

            # ==========================================
            # AI Appointment Recommendation
            # ==========================================

            print("Generating AI Appointment Recommendation...")

            recommendation = AppointmentRecommendation.generate(
                priority=result["priority"],
                qualification_status=result["qualification_status"],
                follow_up_in_hours=result["follow_up_in_hours"],
                vehicle_interest=lead.vehicle_interest,
                purchase_timeline=lead.purchase_timeline,
            )

            print("Appointment Recommendation:")
            print(recommendation)


        except Exception as e:
            print(f"AI Error: {type(e).__name__}: {e}")

            result = {
                "lead_score": 50,
                "qualification_status": "Warm",
                "pipeline_stage": "Follow Up",
                "priority": "Medium",
                "recommended_action": "Manual follow-up required.",
                "follow_up_in_hours": 24,
                "reason": "AI service unavailable. Rule engine fallback used.",
                "tags": [
                    "Manual Review",
                    "Warm Lead"
                ],
                "notes": (
                    "AI qualification service was unavailable. "
                    "Please review this lead manually."
                )
            }

            communication = {
                "email_subject": "Thank you for your enquiry",
                "email_body": (
                    f"Dear {lead.full_name},\n\n"
                    "Thank you for your interest. Our sales team will contact you shortly.\n\n"
                    "Regards,\nSales Team"
                ),
                "whatsapp_message": (
                    f"Hi {lead.full_name}, thank you for your enquiry. "
                    "Our sales team will connect with you soon."
                )
            }
            recommendation = AppointmentRecommendation.generate(
                priority=result["priority"],
                qualification_status=result["qualification_status"],
                follow_up_in_hours=result["follow_up_in_hours"],
                vehicle_interest=lead.vehicle_interest,
                purchase_timeline=lead.purchase_timeline,
        )

            print("Fallback Rule Engine Used.")

        # ==========================================
        # Save Lead
        # ==========================================

        print("Saving Lead...")

        db_lead = LeadRepository.create(db, lead)

        db_lead.lead_score = result["lead_score"]
        db_lead.qualification_status = result["qualification_status"]
        db_lead.pipeline_stage = result["pipeline_stage"]

        db_lead.priority = result["priority"]
        db_lead.recommended_action = result["recommended_action"]
        db_lead.follow_up_in_hours = result["follow_up_in_hours"]
        db_lead.ai_reason = result["reason"]

        db_lead.tags = ", ".join(result["tags"])
        db_lead.notes = result["notes"]

        # ==========================================
        # Save AI Appointment Recommendation
        # ==========================================

        db_lead.suggested_appointment_at = recommendation[
            "suggested_appointment_at"
        ]

        db_lead.suggested_meeting_type = recommendation[
            "suggested_meeting_type"
        ]

        db_lead.appointment_recommendation_status = recommendation[
            "appointment_recommendation_status"
        ]

        db.commit()
        db.refresh(db_lead)

        print("Lead Saved Successfully.")

        # ==========================================
        # Google Sheet Sync
        # ==========================================

        print("\nTrying Google Sheet Sync...")

        try:

            GoogleSheetService.append_lead(db_lead)

            print("Google Sheet Sync Completed.")

        except Exception as e:
            print(f"Google Sheet Sync Failed: {type(e).__name__}: {e}")

        try:
            AutomationService.process_new_lead(
                db,
                db_lead,
                communication
            )

        except Exception as e:
            print(f"Automation Error: {type(e).__name__}: {e}")

        # ==========================================
        # Activity Log
        # ==========================================

        print("Saving Activity Log...")

        ActivityService.log(
            db=db,
            lead_id=db_lead.id,
            activity_type="Lead Created",
            description=(
                f"Lead Created | "
                f"Score: {result['lead_score']} | "
                f"Qualification: {result['qualification_status']} | "
                f"Pipeline: {result['pipeline_stage']}"
            ),
        )

        print("Activity Saved.")

        print("================ END =================\n")

        return db_lead

    @staticmethod
    def get_all_leads(db: Session):
        return LeadRepository.get_all(db)

    @staticmethod
    def get_lead_by_id(db: Session, lead_id: str):

        lead = LeadRepository.get_by_id(db, lead_id)

        if not lead:
            raise HTTPException(
                status_code=404,
                detail="Lead not found"
            )

        return lead

    @staticmethod
    def update_lead(
        db: Session,
        lead_id: str,
        lead: LeadUpdate
    ):

        db_lead = LeadRepository.get_by_id(
            db,
            lead_id
        )

        if not db_lead:
            raise HTTPException(
                status_code=404,
                detail="Lead not found"
            )

        data = lead.model_dump(
            exclude_unset=True
        )

        return LeadRepository.update(
            db,
            db_lead,
            data
        )

    @staticmethod
    def delete_lead(
        db: Session,
        lead_id: str
    ):

        db_lead = LeadRepository.get_by_id(
            db,
            lead_id
        )

        if not db_lead:
            raise HTTPException(
                status_code=404,
                detail="Lead not found"
            )

        # ==========================================
        # Delete Child Records
        # ==========================================

        ActivityRepository.delete_by_lead_id(
            db,
            lead_id
        )

        ConversationRepository.delete_by_lead_id(
            db,
            lead_id
        )

        FollowUpRepository.delete_by_lead_id(
            db,
            lead_id
        )

        AppointmentRepository.delete_by_lead_id(
            db,
            lead_id
        )

        # ==========================================
        # Delete Lead
        # ==========================================

        LeadRepository.delete(
            db,
            db_lead
        )

        return {
            "message": "Lead deleted successfully."
        }