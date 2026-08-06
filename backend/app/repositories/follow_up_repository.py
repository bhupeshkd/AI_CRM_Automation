from sqlalchemy.orm import Session

from app.models.follow_up import FollowUp
from app.schemas.follow_up import (
    FollowUpCreate,
    FollowUpUpdate,
)


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

    @staticmethod
    def get_by_id(
        db: Session,
        follow_up_id: str
    ):

        return (
            db.query(FollowUp)
            .filter(
                FollowUp.id == follow_up_id
            )
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        follow_up: FollowUp
    ):

        db.commit()
        db.refresh(follow_up)

        return follow_up


    @staticmethod
    def delete(
        db: Session,
        follow_up: FollowUp
    ):

        db.delete(follow_up)
        db.commit()

    @staticmethod
    def delete_by_lead_id(
        db: Session,
        lead_id: str
    ):

        db.query(FollowUp).filter(
            FollowUp.lead_id == lead_id
        ).delete()

        db.commit()