from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

# Define the User model class that represents the "users" table in the database
class User(Base):
    # Define the name of the table in the database
    __tablename__ = "users"

    # Define the columns of the "users" table with their respective data types and constraints
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))
    age: Mapped[int]