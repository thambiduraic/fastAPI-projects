from fastapi import FastAPI
from app.routes import users

from app.db.session import engine
from app.db.base import Base
from app.models.user import User

# Create the database tables
Base.metadata.create_all(bind=engine)

# Create the FastAPI app and include the user routes
app = FastAPI()
app.include_router(users.router) 
