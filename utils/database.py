from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from .config import settings
import asyncio


class Database:
    engine = create_async_engine(settings.DATABASE_URL, echo=True)
    
    async def execute(self, query, *args):
        async with self.engine.begin() as conn:
            result = await conn.execute(text(query), args)
            await conn.commit()
            return result