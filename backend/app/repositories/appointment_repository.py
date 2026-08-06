from sqlalchemy.orm import Session
from datetime import datetime

from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate


class AppointmentRepository:

    @staticmethod
    def create(db: Session, appointment: AppointmentCreate):

        db_appointment = Appointment(**appointment.model_dump())

        db.add(db_appointment)
        db.commit()
        db.refresh(db_appointment)

        return db_appointment

    @staticmethod
    def get_all(db: Session):

        return db.query(Appointment).all()

    @staticmethod
    def get_by_id(db: Session, appointment_id: str):

        return (
            db.query(Appointment)
            .filter(Appointment.id == appointment_id)
            .first()
        )

    @staticmethod
    def get_by_datetime(
        db: Session,
        appointment_date: datetime
    ):

        return (
            db.query(Appointment)
            .filter(
                Appointment.appointment_date == appointment_date
            )
            .first()
        )

    @staticmethod
    def delete(db: Session, appointment: Appointment):

        db.delete(appointment)
        db.commit()

    @staticmethod
    def update(
        db: Session,
        appointment: Appointment
        ):

        db.commit()
        db.refresh(appointment)

        return appointment

    @staticmethod
    def delete_by_lead_id(
        db: Session,
        lead_id: str
    ):

        db.query(Appointment).filter(
            Appointment.lead_id == lead_id
        ).delete()

        db.commit()