from sqlalchemy.orm import Session

from app.repositories.follow_up_repository import FollowUpRepository
from app.services.activity_service import ActivityService
from app.schemas.follow_up import (
    FollowUpCreate,
    FollowUpUpdate,
)

from fastapi import HTTPException

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

    @staticmethod
    def update_follow_up(
        db: Session,
        follow_up_id: str,
        follow_up_data: FollowUpUpdate
    ):

        follow_up = FollowUpRepository.get_by_id(
            db,
            follow_up_id
        )

        if not follow_up:

            raise HTTPException(
                status_code=404,
                detail="Follow-up not found."
            )

        update_data = follow_up_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():

            setattr(
                follow_up,
                key,
                value
            )

        FollowUpRepository.update(
            db,
            follow_up
        )

        ActivityService.log(
            db=db,
            lead_id=follow_up.lead_id,
            activity_type="Follow-up Updated",
            description="Follow-up updated."
        )

        return follow_up


    @staticmethod
    def delete_follow_up(
        db: Session,
        follow_up_id: str
    ):

        follow_up = FollowUpRepository.get_by_id(
            db,
            follow_up_id
        )

        if not follow_up:

            raise HTTPException(
                status_code=404,
                detail="Follow-up not found."
            )

        ActivityService.log(
            db=db,
            lead_id=follow_up.lead_id,
            activity_type="Follow-up Deleted",
            description="Follow-up deleted."
        )

        FollowUpRepository.delete(
            db,
            follow_up
        )

        return {
            "message": "Follow-up deleted successfully."
        }