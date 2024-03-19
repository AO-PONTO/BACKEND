from datetime import datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, validator, model_validator

from app import error, models, util




__all__ = [
    "PostSalas",
    "GetSalas",
    "PutSalas",
]


class PostSalas(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        escola_uuid (UUID): descrever escola_uuid.
    """
    
    nome: str = Field(None, description="nome Documentar")
    escola_uuid: UUID = Field(None, description="escola_uuid Documentar")
    ano: str = Field(None, description="ano Documentar")
    turno: str = Field(None, description="turno Documentar")
    #     validate_nome= validator("nome", allow_reuse=True)(...)
    #     validate_escola_uuid= validator("escola_uuid", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_salas(self) -> "PostSalas":
        try:
            False
            pass
            return self
        except Exception as e:
            raise error.custom_HTTPException(e)



class GetSalas(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        escola_uuid (UUID): descrever escola_uuid.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """
    
    nome: str | None = Field(None, description="nome Documentar")
    ano: str = Field(None, description="ano Documentar")
    turno: str = Field(None, description="turno Documentar")
    escola_uuid: UUID | None = Field(None, description="escola_uuid Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(None, description="updated_at Documentar")
    
    class Config:
        from_attributes = True


class PutSalas(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        escola_uuid (UUID): descrever escola_uuid.
    """
    
    nome: str = Field(None, description="nome Documentar")
    escola_uuid: UUID = Field(None, description="escola_uuid Documentar")
    ano: str = Field(None, description="ano Documentar")
    turno: str = Field(None, description="turno Documentar")