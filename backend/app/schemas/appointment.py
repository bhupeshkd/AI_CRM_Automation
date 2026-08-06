from datetime import datetime
from pydantic import BaseModel, ConfigDict


class AppointmentCreate(BaseModel):
    lead_id: str
    appointment_date: datetime
    meeting_type: str


class AppointmentUpdate(BaseModel):
    appointment_date: datetime | None = None
    meeting_type: str | None = None
    status: str | None = None


class AppointmentResponse(BaseModel):
    id: str
    lead_id: str
    appointment_date: datetime
    status: str
    meeting_type: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes = True
    )