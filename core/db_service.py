from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from core.config import DATABASE_URL


async_engine = create_async_engine(DATABASE_URL, echo=True, future=True)


async def init_db(before_drop=False):
    """Init DB."""
    async with async_engine.begin() as conn:
        if before_drop:
            await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    """Get session on DB."""
    async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
