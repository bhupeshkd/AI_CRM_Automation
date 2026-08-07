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
    @staticmethod
    def delete_by_lead_id(
        db: Session,
        lead_id: str
    ):

        db.query(Activity).filter(
            Activity.lead_id == lead_id
        ).delete()

        db.commit()

    @staticmethod
    def get_all(
        db: Session
    ):
        return (
            db.query(Activity)
            .order_by(Activity.created_at.desc())
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        activity_id: str
    ):
        return (
            db.query(Activity)
            .filter(Activity.id == activity_id)
            .first()
        )