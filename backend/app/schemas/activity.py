from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ActivityResponse(BaseModel):

    id: str
    lead_id: str

    activity_type: str
    description: str

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )