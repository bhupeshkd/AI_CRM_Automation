from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.lead import Lead
from app.repositories.appointment_repository import AppointmentRepository
from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentUpdate,
)
from app.services.activity_service import ActivityService
from app.services.automation_service import AutomationService


class AppointmentService:

    @staticmethod
    def create_appointment(
        db: Session,
        appointment: AppointmentCreate
    ):

        # ==========================
        # Check Lead Exists
        # ==========================
        lead = (
            db.query(Lead)
            .filter(Lead.id == appointment.lead_id)
            .first()
        )

        if not lead:
            raise HTTPException(
                status_code=404,
                detail="Lead not found."
            )

        # ==========================
        # Prevent Double Booking
        # ==========================
        existing = AppointmentRepository.get_by_datetime(
            db,
            appointment.appointment_date
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Appointment slot already booked."
            )

        # ==========================
        # Create Appointment
        # ==========================
        db_appointment = AppointmentRepository.create(
            db,
            appointment
        )

        # ==========================
        # Activity Log
        # ==========================
        ActivityService.log(
            db=db,
            lead_id=appointment.lead_id,
            activity_type="Appointment Scheduled",
            description=(
                f"{appointment.meeting_type} scheduled on "
                f"{appointment.appointment_date}"
            )
        )

        return db_appointment

    @staticmethod
    def get_all_appointments(
        db: Session
        ):
        return AppointmentRepository.get_all(db)

    @staticmethod
    def get_appointment_by_id(
        db: Session,
        appointment_id: str
    ):

        appointment = AppointmentRepository.get_by_id(
            db,
            appointment_id
        )

        if not appointment:
            raise HTTPException(
                status_code=404,
                detail="Appointment not found."
            )

        return appointment

    @staticmethod
    def update_appointment(
        db: Session,
        appointment_id: str,
        appointment_data: AppointmentUpdate
    ):

        appointment = AppointmentRepository.get_by_id(
            db,
            appointment_id
        )

        if not appointment:
            raise HTTPException(
                status_code=404,
                detail="Appointment not found."
            )

        # ==========================
        # Update Only Provided Fields
        # ==========================

        update_data = appointment_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                appointment,
                key,
                value
            )

        AppointmentRepository.update(
            db,
            appointment
        )

        # ==========================
        # Missed Appointment Automation
        # ==========================

        if appointment.status.lower() == "missed":
            AutomationService.handle_missed_appointment(
                db,
                appointment
            )

        # ==========================
        # Activity Log
        # ==========================

        ActivityService.log(
            db=db,
            lead_id=appointment.lead_id,
            activity_type="Appointment Updated",
            description=(
                f"Appointment status changed to "
                f"{appointment.status}"
            )
        )

        return appointment

    @staticmethod
    def delete_appointment(
        db: Session,
        appointment_id: str
    ):

        appointment = AppointmentRepository.get_by_id(
            db,
            appointment_id
        )

        if not appointment:

            raise HTTPException(
                status_code=404,
                detail="Appointment not found."
            )

        ActivityService.log(
            db=db,
            lead_id=appointment.lead_id,
            activity_type="Appointment Deleted",
            description=(
                f"{appointment.meeting_type} appointment deleted."
            )
        )

        AppointmentRepository.delete(
            db,
            appointment
        )

        return {
            "message": "Appointment deleted successfully."
        }