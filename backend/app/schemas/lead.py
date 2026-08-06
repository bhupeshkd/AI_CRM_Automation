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

    # ==========================
    # CRM Fields
    # ==========================

    notes: str | None = None
    tags: str | None = None


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

    # ==========================
    # AI Qualification
    # ==========================

    lead_score: int
    qualification_status: str
    pipeline_stage: str

    priority: str
    recommended_action: str | None = None
    follow_up_in_hours: int
    ai_reason: str | None = None

    # ==========================
    # CRM Fields
    # ==========================

    notes: str | None = None
    tags: str | None = None

    # ==========================
    # Audit
    # ==========================

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )

class LeadUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    city: str | None = None
    vehicle_interest: str | None = None
    budget: int | None = None
    purchase_timeline: str | None = None
    lead_source: str | None = None

    notes: str | None = None
    tags: str | None = None