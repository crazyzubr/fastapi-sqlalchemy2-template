from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db_service import get_session
from core.models import Some


api_v1_router = APIRouter(prefix='/api/v1', tags=['Sample API v1'])


@api_v1_router.get("/somes", response_model=list[Some])
async def get_somes(session: AsyncSession = Depends(get_session)):
    """Get somes."""
    result = await session.execute(select(Some))
    somes = result.scalars().all()
    return [
        Some(other_field=x.other_field, id=x.id, updated_at=x.updated_at, created_at=x.created_at)
        for x in somes]
