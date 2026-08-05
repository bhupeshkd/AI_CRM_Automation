from datetime import datetime

from pydantic import BaseModel


class ConversationCreate(BaseModel):
    lead_id: str
    sender: str
    message: str
    message_type: str = "Note"


class ConversationResponse(BaseModel):
    id: str
    lead_id: str
    sender: str
    message: str
    message_type: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }