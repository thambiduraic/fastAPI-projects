from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.user import UserCreate
from app.services.user_services import create_user_service

# Create a new APIRouter instance for user-related routes
router = APIRouter(
    prefix="/users",
)

@router.post("/")
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):

    # Call the service layer to create a new user
    result = create_user_service(
        db=db,
        name=user.username,
        email=user.email,
        age=user.age
    )
    # Return the result of the user creation
    return result
