# from sqlalchemy.orm import Session

# from app.repositories.conversation_repository import ConversationRepository
# from app.schemas.conversation import ConversationCreate


# class ConversationService:

#     @staticmethod
#     def create_conversation(
#         db: Session,
#         conversation: ConversationCreate
#     ):
#         return ConversationRepository.create(
#             db,
#             conversation
#         )

#     @staticmethod
#     def get_all_conversations(
#         db: Session
#     ):
#         return ConversationRepository.get_all(db)

#     @staticmethod
#     def get_conversation_by_lead(
#         db: Session,
#         lead_id: str
#     ):
#         return ConversationRepository.get_by_lead(
#             db,
#             lead_id
#         )

from sqlalchemy.orm import Session

from app.repositories.conversation_repository import ConversationRepository
from app.schemas.conversation import ConversationCreate
from app.services.activity_service import ActivityService


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