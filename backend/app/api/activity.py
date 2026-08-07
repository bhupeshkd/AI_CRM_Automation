from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.activity import ActivityResponse
from app.services.activity_service import ActivityService

router = APIRouter()


@router.get(
    "/",
    response_model=list[ActivityResponse]
)
def get_all_activities(
    db: Session = Depends(get_db)
):
    return ActivityService.get_all(db)


@router.get(
    "/{activity_id}",
    response_model=ActivityResponse
)
def get_activity(
    activity_id: str,
    db: Session = Depends(get_db)
):

    activity = ActivityService.get_by_id(
        db,
        activity_id
    )

    if not activity:
        raise HTTPException(
            status_code=404,
            detail="Activity not found"
        )

    return activity