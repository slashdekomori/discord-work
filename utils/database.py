from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from .config import settings
import asyncio
# Таблица workers
# discord_id: str ; index = 0
# penalty: int ; index = 1

class Database:
    engine = create_async_engine(settings.DATABASE_URL)

    async def add_worker_if_not_exists(self,id: str):
        async with self.engine.connect() as conn:
                await conn.execute(text("INSERT INTO workers (discord_id, penalty) VALUES (:id, 0)"), {"id": id})
                await conn.commit()

    async def worker_exists(self,id: str):
            async with self.engine.connect() as conn:
                result = await conn.execute(text("SELECT 1 FROM workers WHERE discord_id = :id"), {"id": id})
                return result.first() is not None
            
        
    async def get_workers(self,id: str):
        async with self.engine.connect() as conn:
            if not await self.worker_exists(id):
                await self.add_worker_if_not_exists(id)
            result = await conn.execute(text("SELECT * FROM workers WHERE discord_id = :id"), {"id": id})
            return result.first()
        