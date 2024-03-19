from datetime import datetime, date
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, validator, model_validator

from app import error, models, util




__all__ = [
    "PostAlunos",
    "GetAlunos",
    "PutAlunos",
]


class PostAlunos(BaseModel):
    """__summary__

    Attributes:
        escola_uuid (UUID): descrever escola_uuid.
        escola_name (str): descrever escola_name.
        matricula (int): descrever matricula.
        nome (str): descrever nome.
        data_nascimento (date): descrever data_nascimento.
    """
    
    escola_uuid: UUID = Field(None, description="escola_uuid Documentar")
    escola_name: str = Field(None, description="escola_name Documentar")
    matricula: int = Field(None, description="matricula Documentar")
    nome: str = Field(None, description="nome Documentar")
    data_nascimento: date = Field(None, description="data_nascimento Documentar")
    
    #     validate_escola_uuid= validator("escola_uuid", allow_reuse=True)(...)
    #     validate_escola_name= validator("escola_name", allow_reuse=True)(...)
    #     validate_matricula= validator("matricula", allow_reuse=True)(...)
    #     validate_nome= validator("nome", allow_reuse=True)(...)
    #     validate_data_nascimento= validator("data_nascimento", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_alunos(self) -> "PostAlunos":
        try:
            False
            pass
            return self
        except Exception as e:
            raise error.custom_HTTPException(e)


    @classmethod
    def as_form(
        cls,
        escola_uuid: UUID = Form(None, description="escola_uuid Documentar"),
        escola_name: str = Form(None, description="escola_name Documentar"),
        matricula: int = Form(None, description="matricula Documentar"),
        nome: str = Form(None, description="nome Documentar"),
        data_nascimento: date = Form(None, description="data_nascimento Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            escola_uuid=escola_uuid,
            escola_name=escola_name,
            matricula=matricula,
            nome=nome,
            data_nascimento=data_nascimento,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetAlunos(BaseModel):
    """__summary__

    Attributes:
        escola_uuid (UUID): descrever escola_uuid.
        escola_name (str): descrever escola_name.
        matricula (int): descrever matricula.
        nome (str): descrever nome.
        data_nascimento (date): descrever data_nascimento.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """
    
    escola_uuid: UUID | None = Field(None, description="escola_uuid Documentar")
    escola_name: str | None = Field(None, description="escola_name Documentar")
    matricula: int | None = Field(None, description="matricula Documentar")
    nome: str | None = Field(None, description="nome Documentar")
    data_nascimento: date | None = Field(None, description="data_nascimento Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(None, description="updated_at Documentar")
    
    class Config:
        from_attributes = True


class PutAlunos(BaseModel):
    """__summary__

    Attributes:
        escola_uuid (UUID): descrever escola_uuid.
        escola_name (str): descrever escola_name.
        matricula (int): descrever matricula.
        nome (str): descrever nome.
        data_nascimento (date): descrever data_nascimento.
    """
    
    escola_uuid: UUID = Field(None, description="escola_uuid Documentar")
    escola_name: str = Field(None, description="escola_name Documentar")
    matricula: int = Field(None, description="matricula Documentar")
    nome: str = Field(None, description="nome Documentar")
    data_nascimento: date = Field(None, description="data_nascimento Documentar")