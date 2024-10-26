from .logger import logging
from app.db import Base

__all__ = ["Base"]


logging.info("Initializing the app package")