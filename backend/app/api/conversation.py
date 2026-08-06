from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.models.user import User

from app.database.database import get_db

from app.schemas.conversation import (
    ConversationCreate,
    ConversationUpdate,
    ConversationResponse,
)

from app.services.conversation_service import ConversationService

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)


@router.post(
    "/",
    response_model=ConversationResponse,
    status_code=201
)
def create_conversation(
    conversation: ConversationCreate,
    db: Session = Depends(get_db),
    # current_user: User = Depends(get_current_user)
):
    return ConversationService.create_conversation(
        db,
        conversation
    )


@router.get(
    "/",
    response_model=list[ConversationResponse]
)
def get_all_conversations(
    db: Session = Depends(get_db)
):
    return ConversationService.get_all_conversations(db)


@router.get(
    "/lead/{lead_id}",
    response_model=list[ConversationResponse]
)
def get_conversation_by_lead(
    lead_id: str,
    db: Session = Depends(get_db)
):
    return ConversationService.get_conversation_by_lead(
        db,
        lead_id
    )


@router.patch(
    "/{conversation_id}",
    response_model=ConversationResponse
)
def update_conversation(
    conversation_id: str,
    conversation: ConversationUpdate,
    db: Session = Depends(get_db),
):

    return ConversationService.update_conversation(
        db,
        conversation_id,
        conversation
    )


@router.delete(
    "/{conversation_id}"
)
def delete_conversation(
    conversation_id: str,
    db: Session = Depends(get_db),
):

    return ConversationService.delete_conversation(
        db,
        conversation_id
    )