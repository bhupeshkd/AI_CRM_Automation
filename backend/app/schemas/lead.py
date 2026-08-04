from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class LeadCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    city: str
    vehicle_interest: str
    budget: int
    purchase_timeline: str
    lead_source: str = "Website"


class LeadResponse(BaseModel):
    id: str
    full_name: str
    email: EmailStr
    phone: str
    city: str
    vehicle_interest: str
    budget: int
    purchase_timeline: str
    lead_source: str
    lead_score: int
    qualification_status: str
    pipeline_stage: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)