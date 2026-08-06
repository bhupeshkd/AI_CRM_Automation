from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import (
    UserCreate,
    UserLogin,
)


class AuthService:

    @staticmethod
    def register(
        db: Session,
        user: UserCreate
    ):

        # ==========================
        # Duplicate Email Check
        # ==========================

        existing_user = UserRepository.get_by_email(
            db,
            user.email
        )

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="User already exists with this email."
            )

        # ==========================
        # Duplicate Phone Check
        # ==========================

        existing_phone = UserRepository.get_by_phone(
            db,
            user.phone
        )

        if existing_phone:
            raise HTTPException(
                status_code=400,
                detail="User already exists with this phone number."
            )
        # ==========================
        # Create User
        # ==========================

        db_user = User(
                full_name=user.full_name,
                email=user.email,
                phone=user.phone,
                password_hash=hash_password(
                    user.password
                ),
                role=user.role
            )

        return UserRepository.create(
            db,
            db_user
        )

    @staticmethod
    def login(
        db: Session,
        user: UserLogin
    ):

        db_user = UserRepository.get_by_email(
            db,
            user.email
        )

        if not db_user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password."
            )

        if not verify_password(
            user.password,
            db_user.password_hash
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password."
            )

        # ==========================
        # Active User Check
        # ==========================

        if not db_user.is_active:
            raise HTTPException(
                status_code=403,
                detail="Your account has been deactivated."
            )

        token = create_access_token(
            {
                "sub": db_user.email,
                "role": db_user.role,
                "user_id": db_user.id,
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }