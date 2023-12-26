from typing import Callable, Generator
from uuid import uuid4

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from core.app import app
from core.db_service import async_engine
from core.models import Some


@pytest_asyncio.fixture
async def async_client(async_session: AsyncSession) -> Generator:
    async with AsyncClient(
        app=app,
        base_url='http://localhost/',
    ) as client:
        yield client


@pytest_asyncio.fixture(scope='function')
async def async_session() -> AsyncSession:
    _async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
    async with _async_session() as _sess:
        async with async_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
        yield _sess
        async with async_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)
    await async_engine.dispose()


@pytest_asyncio.fixture(scope='function')
async def some_factory(async_session: AsyncSession) -> Callable:

    async def create(**kwargs):
        params = dict(
            other_field=f'Test value {uuid4()}',
        )
        params.update(kwargs)
        some = Some(**params)
        async_session.add(some)
        await async_session.commit()
        return some

    return create
