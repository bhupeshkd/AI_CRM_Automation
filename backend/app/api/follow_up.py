from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.follow_up_service import FollowUpService
from app.schemas.follow_up import (
    FollowUpCreate,
    FollowUpUpdate,
    FollowUpResponse,
)

# from app.models.user import User
# from app.core.security import get_current_user


router = APIRouter(
    prefix="/follow-ups",
    tags=["Follow Ups"]
)


@router.post(
    "/",
    response_model=FollowUpResponse,
    status_code=201
)
def create_follow_up(
    follow_up: FollowUpCreate,
    db: Session = Depends(get_db),
    # current_user: User = Depends(get_current_user)
):
    return FollowUpService.create_follow_up(
        db,
        follow_up
    )


@router.get(
    "/",
    response_model=list[FollowUpResponse]
)
def get_all_follow_ups(
    db: Session = Depends(get_db)
):
    return FollowUpService.get_all_follow_ups(db)


@router.get(
    "/lead/{lead_id}",
    response_model=list[FollowUpResponse]
)
def get_follow_ups_by_lead(
    lead_id: str,
    db: Session = Depends(get_db)
):
    return FollowUpService.get_follow_ups_by_lead(
        db,
        lead_id
    )

@router.patch(
    "/{follow_up_id}",
    response_model=FollowUpResponse
)
def update_follow_up(
    follow_up_id: str,
    follow_up: FollowUpUpdate,
    db: Session = Depends(get_db),
):

    return FollowUpService.update_follow_up(
        db,
        follow_up_id,
        follow_up
    )


@router.delete(
    "/{follow_up_id}"
)
def delete_follow_up(
    follow_up_id: str,
    db: Session = Depends(get_db),
):

    return FollowUpService.delete_follow_up(
        db,
        follow_up_id
    )