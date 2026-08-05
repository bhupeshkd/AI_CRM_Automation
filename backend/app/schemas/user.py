from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


# ==========================
# Register
# ==========================

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    password: str


# ==========================
# Login
# ==========================

class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ==========================
# Response
# ==========================

class UserResponse(BaseModel):
    id: str
    full_name: str
    email: EmailStr
    phone: str
    role: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================
# JWT Token
# ==========================

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"