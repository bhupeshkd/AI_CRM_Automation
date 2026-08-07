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
    @staticmethod
    def get_all(
        db: Session
    ):
        return ActivityRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db: Session,
        activity_id: str
    ):
        return ActivityRepository.get_by_id(
            db,
            activity_id
        )