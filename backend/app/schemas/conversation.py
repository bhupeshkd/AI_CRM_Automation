from datetime import datetime

from pydantic import BaseModel,ConfigDict


class ConversationCreate(BaseModel):
    lead_id: str
    sender: str
    message: str
    message_type: str = "Note"


class ConversationUpdate(BaseModel):
    sender: str | None = None
    message: str | None = None
    message_type: str | None = None


class ConversationResponse(BaseModel):
    id: str
    lead_id: str
    sender: str
    message: str
    message_type: str
    created_at: datetime

    model_config = ConfigDict(
    from_attributes=True
    )