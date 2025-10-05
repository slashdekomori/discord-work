from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from .config import settings
import asyncio


class Database:
    engine = create_async_engine(settings.DATABASE_URL, echo=True)

    def get_workers(self,id):
        with self.engine.connect() as conn:
            result = conn.execute(text("SELECT penalty FROM workers WHERE id = {id}"))
            return result.fetchall()