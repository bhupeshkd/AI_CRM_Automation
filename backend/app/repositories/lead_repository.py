# from sqlalchemy.orm import Session

# from app.models.lead import Lead
# from app.schemas.lead import LeadCreate


# class LeadRepository:

#     @staticmethod
#     def get_all(db: Session):
#         return db.query(Lead).all()

#     @staticmethod
#     def get_by_id(db: Session, lead_id: str):
#         return db.query(Lead).filter(Lead.id == lead_id).first()

#     @staticmethod
#     def get_by_email(db: Session, email: str):
#         return db.query(Lead).filter(Lead.email == email).first()

#     @staticmethod
#     def get_by_phone(db: Session, phone: str):
#         return db.query(Lead).filter(Lead.phone == phone).first()

#     @staticmethod
#     def create(db: Session, lead: LeadCreate):

#         db_lead = Lead(
#             full_name=lead.full_name,
#             email=lead.email,
#             phone=lead.phone,
#             city=lead.city,
#             vehicle_interest=lead.vehicle_interest,
#             budget=lead.budget,
#             purchase_timeline=lead.purchase_timeline,
#             lead_source=lead.lead_source,

#             # ==========================
#             # CRM Fields
#             # ==========================

#             notes=lead.notes,
#             tags=lead.tags,
#         )

#         db.add(db_lead)
#         db.commit()
#         db.refresh(db_lead)

#         return db_lead

from sqlalchemy.orm import Session

from app.models.lead import Lead
from app.schemas.lead import LeadCreate


class LeadRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(Lead).all()

    @staticmethod
    def get_by_id(
        db: Session,
        lead_id: str
    ):
        return (
            db.query(Lead)
            .filter(Lead.id == lead_id)
            .first()
        )

    @staticmethod
    def get_by_email(
        db: Session,
        email: str
    ):
        return (
            db.query(Lead)
            .filter(Lead.email == email)
            .first()
        )

    @staticmethod
    def get_by_phone(
        db: Session,
        phone: str
    ):
        return (
            db.query(Lead)
            .filter(Lead.phone == phone)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        lead: LeadCreate
    ):
        """
        Create a new lead using all fields
        from the Pydantic schema.
        """

        db_lead = Lead(
            **lead.model_dump()
        )

        db.add(db_lead)
        db.commit()
        db.refresh(db_lead)

        return db_lead