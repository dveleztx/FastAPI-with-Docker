# Imports
import logging
import os
from functools import lru_cache
from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    """
    Environment-specific configuration for our application.

    Attributes:
        environment (str): Defines the environment (i.e dev, stage, prod).
        testing (bool): Defines whether or not we're in test mode.
        database_url (AnyUrl): Defines the database URI path.
    """

    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache()
def get_settings() -> BaseSettings:
    """
    Get the config settings from set environment variables

    :return: Environment settings
    """
    log.info("Loading config settings from the environment...")
    return Settings()
