from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from app.core.security import get_current_user
# from app.models.user import User

from app.database.database import get_db
from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentUpdate,
    AppointmentResponse,
)

from app.services.appointment_service import AppointmentService

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)


@router.post(
    "/",
    response_model=AppointmentResponse,
    status_code=201
)
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db),
    # current_user: User = Depends(get_current_user)
):
    return AppointmentService.create_appointment(
        db,
        appointment
    )


@router.get(
    "/",
    response_model=list[AppointmentResponse]
)
def get_all_appointments(
    db: Session = Depends(get_db)
):
    return AppointmentService.get_all_appointments(db)


@router.get(
    "/{appointment_id}",
    response_model=AppointmentResponse
)
def get_appointment(
    appointment_id: str,
    db: Session = Depends(get_db)
):
    return AppointmentService.get_appointment_by_id(
        db,
        appointment_id
    )

@router.patch(
    "/{appointment_id}",
    response_model=AppointmentResponse
)
def update_appointment(
    appointment_id: str,
    appointment: AppointmentUpdate,
    db: Session = Depends(get_db),
    # current_user: User = Depends(get_current_user)
):
    return AppointmentService.update_appointment(
        db,
        appointment_id,
        appointment
    )

@router.delete(
    "/{appointment_id}"
)
def delete_appointment(
    appointment_id: str,
    db: Session = Depends(get_db),
):

    return AppointmentService.delete_appointment(
        db,
        appointment_id
    )