from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.ai.qualification import LeadQualification
from app.repositories.lead_repository import LeadRepository
from app.schemas.lead import LeadCreate
from app.services.activity_service import ActivityService


class LeadService:

    @staticmethod
    def create_lead(db: Session, lead: LeadCreate):

        if LeadRepository.get_by_email(db, lead.email):
            raise HTTPException(
                status_code=400,
                detail="Lead already exists with this email."
            )

        if LeadRepository.get_by_phone(db, lead.phone):
            raise HTTPException(
                status_code=400,
                detail="Lead already exists with this phone number."
            )

        score, status = LeadQualification.qualify(
            lead.budget,
            lead.purchase_timeline
        )

        db_lead = LeadRepository.create(
            db,
            lead
        )

        db_lead.lead_score = score
        db_lead.qualification_status = status

        if status == "Hot":
            db_lead.pipeline_stage = "Qualified"

        elif status == "Warm":
            db_lead.pipeline_stage = "Follow Up"

        else:
            db_lead.pipeline_stage = "Cold Lead"

        db.commit()
        db.refresh(db_lead)
        ActivityService.log(
            db=db,
            lead_id=db_lead.id,
            activity_type="Lead Created",
            description=f"Lead created with qualification {status}"
        )

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