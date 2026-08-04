from sqlalchemy.orm import Session

from app.models.activity import Activity


class ActivityRepository:

    @staticmethod
    def create(
        db: Session,
        lead_id: str,
        activity_type: str,
        description: str
    ):

        activity = Activity(
            lead_id=lead_id,
            activity_type=activity_type,
            description=description
        )

        db.add(activity)
        db.commit()

        db.refresh(activity)

        return activity