from sqlalchemy.orm import Session

from app.repositories.conversation_repository import ConversationRepository
from app.services.activity_service import ActivityService
from fastapi import HTTPException

from app.schemas.conversation import (
    ConversationCreate,
    ConversationUpdate,
)

class ConversationService:

    @staticmethod
    def create_conversation(
        db: Session,
        conversation: ConversationCreate
    ):
        db_conversation = ConversationRepository.create(
            db,
            conversation
        )

        ActivityService.log(
            db=db,
            lead_id=db_conversation.lead_id,
            activity_type="Conversation Added",
            description=(
                f"{db_conversation.sender} sent a "
                f"{db_conversation.message_type} message."
            ),
        )

        return db_conversation

    @staticmethod
    def get_all_conversations(
        db: Session
    ):
        return ConversationRepository.get_all(db)

    @staticmethod
    def get_conversation_by_lead(
        db: Session,
        lead_id: str
    ):
        return ConversationRepository.get_by_lead(
            db,
            lead_id
        )
    
    @staticmethod
    def update_conversation(
        db: Session,
        conversation_id: str,
        conversation_data: ConversationUpdate
    ):

        conversation = ConversationRepository.get_by_id(
            db,
            conversation_id
        )

        if not conversation:

            raise HTTPException(
                status_code=404,
                detail="Conversation not found."
            )

        update_data = conversation_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():

            setattr(
                conversation,
                key,
                value
            )

        ConversationRepository.update(
            db,
            conversation
        )

        ActivityService.log(
            db=db,
            lead_id=conversation.lead_id,
            activity_type="Conversation Updated",
            description="Conversation updated."
        )

        return conversation


    @staticmethod
    def delete_conversation(
        db: Session,
        conversation_id: str
    ):

        conversation = ConversationRepository.get_by_id(
            db,
            conversation_id
        )

        if not conversation:

            raise HTTPException(
                status_code=404,
                detail="Conversation not found."
            )

        ActivityService.log(
            db=db,
            lead_id=conversation.lead_id,
            activity_type="Conversation Deleted",
            description="Conversation deleted."
        )

        ConversationRepository.delete(
            db,
            conversation
        )

        return {
            "message": "Conversation deleted successfully."
        }