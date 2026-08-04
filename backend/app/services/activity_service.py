from sqlalchemy.orm import Session

from app.repositories.activity_repository import ActivityRepository


class ActivityService:

    @staticmethod
    def log(
        db: Session,
        lead_id: str,
        activity_type: str,
        description: str
    ):

        return ActivityRepository.create(
            db,
            lead_id,
            activity_type,
            description
        )