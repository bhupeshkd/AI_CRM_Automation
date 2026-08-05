from datetime import datetime

from pydantic import BaseModel


class FollowUpCreate(BaseModel):
    lead_id: str
    follow_up_type: str
    scheduled_at: datetime
    remarks: str | None = None


class FollowUpUpdate(BaseModel):
    status: str | None = None
    remarks: str | None = None


class FollowUpResponse(BaseModel):
    id: str
    lead_id: str
    follow_up_type: str
    scheduled_at: datetime
    status: str
    remarks: str | None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }