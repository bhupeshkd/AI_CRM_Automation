from sqlalchemy.orm import Session

from app.repositories.follow_up_repository import FollowUpRepository
from app.schemas.follow_up import FollowUpCreate
from app.services.activity_service import ActivityService


class FollowUpService:

    @staticmethod
    def create_follow_up(
        db: Session,
        follow_up: FollowUpCreate
    ):

        db_follow_up = FollowUpRepository.create(
            db,
            follow_up
        )

        ActivityService.log(
            db=db,
            lead_id=db_follow_up.lead_id,
            activity_type="Follow-up Scheduled",
            description=(
                f"{db_follow_up.follow_up_type} scheduled "
                f"for {db_follow_up.scheduled_at}"
            )
        )

        return db_follow_up

    @staticmethod
    def get_all_follow_ups(
        db: Session
    ):
        return FollowUpRepository.get_all(db)

    @staticmethod
    def get_follow_ups_by_lead(
        db: Session,
        lead_id: str
    ):
        return FollowUpRepository.get_by_lead(
            db,
            lead_id
        )