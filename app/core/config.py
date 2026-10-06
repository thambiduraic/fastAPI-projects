from pydantic_settings import BaseSettings

# Define a Settings class that inherits from BaseSettings to manage configuration values
class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

# Create an instance of the Settings class to access the configuration values
settings = Settings()