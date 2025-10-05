from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from config import settings

import asyncio
engine = create_async_engine(settings.DATABASE_URL, echo=True)
async def main():
    async with engine.connect() as conn:
        await conn.execute(text("DELETE FROM workers"))
        await conn.commit()


asyncio.run(main())