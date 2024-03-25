from datetime import datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, model_validator, validator

from app import error, models, util

__all__ = [
    "PostFrequencias",
    "GetFrequencias",
    "PutFrequencias",
]


class PostFrequencias(BaseModel):
    """__summary__

    Attributes:
        aluno_turmas_uuid (UUID): descrever aluno_turmas_uuid.
        chamada (bool): descrever chamada.
        data (int): descrever data.
    """

    aluno_turmas_uuid: UUID = Field(
        ..., description="aluno_turmas_uuid Documentar"
    )
    chamada: bool = Field(None, description="chamada Documentar")
    data: str = Field(None, description="data Documentar")
    hora: str = Field(None, description="data Documentar")

class GetFrequencias(BaseModel):
    """__summary__

    Attributes:
        aluno_turmas_uuid (UUID): descrever aluno_turmas_uuid.
        chamada (bool): descrever chamada.
        data (int): descrever data.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """

    aluno_turmas_uuid: UUID = Field(
        ..., description="aluno_turmas_uuid Documentar"
    )
    chamada: bool | None = Field(None, description="chamada Documentar")
    data: str = Field(None, description="data Documentar")
    hora: str = Field(None, description="data Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(
        None, description="updated_at Documentar"
    )

    class Config:
        from_attributes = True


class PutFrequencias(BaseModel):
    """__summary__

    Attributes:
        aluno_turmas_uuid (UUID): descrever aluno_turmas_uuid.
        chamada (bool): descrever chamada.
        data (int): descrever data.
    """

    aluno_turmas_uuid: UUID = Field(
        None, description="aluno_turmas_uuid Documentar"
    )
    chamada: bool = Field(None, description="chamada Documentar")
    data: str = Field(None, description="data Documentar")
    hora: str = Field(None, description="data Documentar")
