from sqlalchemy.orm import Session
from app.models.user import User

# Define a repository function to create a new user in the database
def create_user(db: Session, username: str, email: str, age: int):
    # Create a new user instance and add it to the database
    new_user = User(username=username, email=email, age=age)

    # Add the new user to the database session, commit the transaction, and refresh the instance to get the updated data
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Return the newly created user instance
    return new_user