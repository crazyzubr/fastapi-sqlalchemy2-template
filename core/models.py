from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, Column, text
from sqlmodel import Field, SQLModel


__all__ = ('Some', )


class BaseModel(SQLModel):
    id: Optional[int] = Field(
        default=None, sa_column=Column(BigInteger(), primary_key=True, autoincrement=True))
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False,
        sa_column_kwargs=dict(server_default=text('current_timestamp(0)')),
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False,
        sa_column_kwargs=dict(
            server_default=text('current_timestamp(0)'),
            onupdate=text('current_timestamp(0)'),
        ))


class Some(BaseModel, table=True):
    """Some model."""

    other_field: str


class SomeCreate(BaseModel):
    pass
