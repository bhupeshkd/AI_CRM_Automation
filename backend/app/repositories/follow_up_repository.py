from sqlalchemy.orm import Session

from app.models.follow_up import FollowUp
from app.schemas.follow_up import FollowUpCreate


class FollowUpRepository:

    @staticmethod
    def create(
        db: Session,
        follow_up: FollowUpCreate
    ):
        db_follow_up = FollowUp(
            **follow_up.model_dump()
        )

        db.add(db_follow_up)
        db.commit()
        db.refresh(db_follow_up)

        return db_follow_up

    @staticmethod
    def get_all(db: Session):
        return db.query(FollowUp).all()

    @staticmethod
    def get_by_lead(
        db: Session,
        lead_id: str
    ):
        return (
            db.query(FollowUp)
            .filter(FollowUp.lead_id == lead_id)
            .all()
        )