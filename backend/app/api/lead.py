from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.models.user import User

from app.database.database import get_db
from app.schemas.lead import LeadCreate, LeadResponse
from app.services.lead_service import LeadService

router = APIRouter(
    prefix="/leads",
    tags=["Leads"],
)


@router.post(
    "/",
    response_model=LeadResponse,
    status_code=201
)
def create_lead(
    lead: LeadCreate,
    db: Session = Depends(get_db),
    # current_user: User = Depends(get_current_user)
):
    return LeadService.create_lead(db, lead)

@router.get(
    "/",
    response_model=list[LeadResponse]
)
def get_all_leads(
    db: Session = Depends(get_db)
):
    return LeadService.get_all_leads(db)


@router.get(
    "/{lead_id}",
    response_model=LeadResponse
)
def get_lead(
    lead_id: str,
    db: Session = Depends(get_db)
):
    return LeadService.get_lead_by_id(
        db,
        lead_id
    )

