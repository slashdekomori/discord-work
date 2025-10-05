from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from .config import settings
import asyncio


class Database:
    engine = create_async_engine(settings.DATABASE_URL, echo=True)
    