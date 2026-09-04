from sqlalchemy.orm import Session
from app.repositories.user_repositories import create_user

# Define a service function to handle user creation
def create_user_service(db: Session, name: str, email: str, age: int):
    
    # Call the repository function to create a new user in the database
    user = create_user(db=db, username=name, email=email, age=age)

    # Return the created user object
    return user