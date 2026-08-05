# from datetime import datetime, timedelta

# from sqlalchemy.orm import Session

# from app.models.appointment import Appointment
# from app.models.lead import Lead
# from app.schemas.follow_up import FollowUpCreate
# from app.services.follow_up_service import FollowUpService

# from app.schemas.conversation import ConversationCreate
# from app.services.conversation_service import ConversationService


# class AutomationService:

#     @staticmethod
#     def process_new_lead(
#         db: Session,
#         lead: Lead
#     ):
#         """
#         Main automation workflow executed
#         after a new lead is created.
#         """
#         if AutomationService.check_exit_condition(
#             lead
#         ):
#             return

#         follow_up_time = datetime.utcnow() + timedelta(
#             hours=lead.follow_up_in_hours
#         )

#         # ==========================
#         # Decide Follow-up Type
#         # ==========================

#         if lead.priority == "High":
#             follow_up_type = "Call"

#         elif lead.priority == "Medium":
#             follow_up_type = "WhatsApp"

#         else:
#             follow_up_type = "Email"

#         # ==========================
#         # Create Follow-up
#         # ==========================

#         FollowUpService.create_follow_up(
#             db,
#             FollowUpCreate(
#                 lead_id=lead.id,
#                 follow_up_type=follow_up_type,
#                 scheduled_at=follow_up_time,
#                 remarks=lead.recommended_action
#             )
#         )

#     @staticmethod
#     def handle_missed_appointment(
#         db: Session,
#         appointment: Appointment
#     ):
#         """
#         Handle missed appointments
#         """

#         # ==========================
#         # Create Follow-up
#         # ==========================

#         follow_up_time = appointment.appointment_date + timedelta(days=1)

#         FollowUpService.create_follow_up(
#             db,
#             FollowUpCreate(
#                 lead_id=appointment.lead_id,
#                 follow_up_type="Call",
#                 scheduled_at=follow_up_time,
#                 remarks=(
#                     "Customer missed the appointment. "
#                     "Call and reschedule the test drive."
#                 )
#             )
#         )

#         # ==========================
#         # AI Re-engagement Message
#         # ==========================

#         ConversationService.create_conversation(
#             db,
#             ConversationCreate(
#                 lead_id=appointment.lead_id,
#                 sender="AI",
#                 message=(
#                     "We noticed you couldn't attend your scheduled "
#                     "test drive. Reply to this message and we'll help "
#                     "you book another convenient slot."
#                 ),
#                 message_type="WhatsApp"
#             )
#         )

#         # ==========================
#         # Move Lead to Re-engagement
#         # ==========================

#         lead = (
#             db.query(Lead)
#             .filter(Lead.id == appointment.lead_id)
#             .first()
#         )

#         if lead:
#             lead.pipeline_stage = "Re-engagement"
#             db.commit()

#     @staticmethod
#     def check_exit_condition(
#         lead: Lead
#     ):
#         """
#         Stop automation if lead
#         is converted or inactive.
#         """

#         if lead.pipeline_stage in [
#             "Won",
#             "Lost",
#             "Closed",
#         ]:
#             return True

#         return False
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.appointment import Appointment
from app.models.lead import Lead
from app.schemas.conversation import ConversationCreate
from app.schemas.follow_up import FollowUpCreate
from app.services.activity_service import ActivityService
from app.services.conversation_service import ConversationService
from app.services.follow_up_service import FollowUpService


class AutomationService:

    @staticmethod
    def process_new_lead(
        db: Session,
        lead: Lead
    ):
        """
        Main automation workflow executed
        after a new lead is created.
        """

        # ==========================
        # Exit Condition
        # ==========================

        if AutomationService.check_exit_condition(lead):

            ActivityService.log(
                db=db,
                lead_id=lead.id,
                activity_type="Automation Skipped",
                description=(
                    "Lead is already closed. "
                    "No automation executed."
                )
            )

            return

        # ==========================
        # Follow-up Time
        # ==========================

        follow_up_time = datetime.utcnow() + timedelta(
            hours=lead.follow_up_in_hours
        )

        # ==========================
        # Decide Follow-up Type
        # ==========================

        if lead.priority == "High":
            follow_up_type = "Call"

        elif lead.priority == "Medium":
            follow_up_type = "WhatsApp"

        else:
            follow_up_type = "Email"

        # ==========================
        # Create Follow-up
        # ==========================

        FollowUpService.create_follow_up(
            db,
            FollowUpCreate(
                lead_id=lead.id,
                follow_up_type=follow_up_type,
                scheduled_at=follow_up_time,
                remarks=lead.recommended_action
            )
        )

    @staticmethod
    def handle_missed_appointment(
        db: Session,
        appointment: Appointment
    ):
        """
        Handle missed appointments
        """

        lead = (
            db.query(Lead)
            .filter(Lead.id == appointment.lead_id)
            .first()
        )

        if not lead:
            return

        # ==========================
        # Exit Condition
        # ==========================

        if AutomationService.check_exit_condition(lead):

            ActivityService.log(
                db=db,
                lead_id=lead.id,
                activity_type="Automation Skipped",
                description=(
                    "Lead is already closed. "
                    "Missed appointment workflow skipped."
                )
            )

            return

        # ==========================
        # Create Follow-up
        # ==========================

        follow_up_time = (
            appointment.appointment_date +
            timedelta(days=1)
        )

        FollowUpService.create_follow_up(
            db,
            FollowUpCreate(
                lead_id=appointment.lead_id,
                follow_up_type="Call",
                scheduled_at=follow_up_time,
                remarks=(
                    "Customer missed the appointment. "
                    "Call and reschedule the test drive."
                )
            )
        )

        # ==========================
        # AI WhatsApp Message
        # ==========================

        ConversationService.create_conversation(
            db,
            ConversationCreate(
                lead_id=appointment.lead_id,
                sender="AI",
                message=(
                    "We noticed you couldn't attend your "
                    "scheduled test drive. Reply to this "
                    "message and we'll help you book "
                    "another convenient slot."
                ),
                message_type="WhatsApp"
            )
        )

        # ==========================
        # Update Pipeline
        # ==========================

        lead.pipeline_stage = "Re-engagement"

        db.commit()
        db.refresh(lead)

    @staticmethod
    def check_exit_condition(
        lead: Lead
    ):
        """
        Stop automation if lead
        is converted or inactive.
        """

        return lead.pipeline_stage in [
            "Won",
            "Lost",
            "Closed",
        ]