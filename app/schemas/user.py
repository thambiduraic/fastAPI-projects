from pydantic import BaseModel

# Define a Pydantic model for user creation
class UserCreate(BaseModel):
    username: str
    email: str
    age: int