from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from app.schemas.conversation import (
    ConversationCreate,
    ConversationUpdate,
)


class ConversationRepository:

    @staticmethod
    def create(
        db: Session,
        conversation: ConversationCreate
    ):
        db_conversation = Conversation(
            **conversation.model_dump()
        )

        db.add(db_conversation)
        db.commit()
        db.refresh(db_conversation)

        return db_conversation

    @staticmethod
    def get_all(
        db: Session
    ):
        return db.query(
            Conversation
        ).all()

    @staticmethod
    def get_by_lead(
        db: Session,
        lead_id: str
    ):
        return (
            db.query(Conversation)
            .filter(
                Conversation.lead_id == lead_id
            )
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        conversation_id: str
    ):

        return (
            db.query(Conversation)
            .filter(
                Conversation.id == conversation_id
            )
            .first()
        )


    @staticmethod
    def update(
        db: Session,
        conversation: Conversation
    ):

        db.commit()
        db.refresh(conversation)

        return conversation


    @staticmethod
    def delete(
        db: Session,
        conversation: Conversation
    ):

        db.delete(conversation)
        db.commit()

    @staticmethod
    def delete_by_lead_id(
        db: Session,
        lead_id: str
    ):

        db.query(Conversation).filter(
            Conversation.lead_id == lead_id
        ).delete()

        db.commit()