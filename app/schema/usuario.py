from datetime import date, datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, model_validator, validator

from app import error, models, util

__all__ = [
    "PostUsuario",
    "GetUsuario",
    "PutUsuario",
]


class PostUsuario(BaseModel):
    """__summary__

    Attributes:
        cpf (str): descrever cpf.
        senha (str): descrever senha.
        email (str): descrever email.
        data_nascimento (date): descrever data_nascimento.
        active (bool): descrever active.
        escola_uuid (UUID): descrever escola_uuid.
        papel_uuid (UUID): descrever papel_uuid.
        escola_name (str): descrever escola_name.
        papel_name (str): descrever papel_name.
        access_level (str): descrever access_level.
    """

    cpf: str = Field(None, description="cpf Documentar", max_length=11)
    senha: bytes = Field(None, description="senha Documentar")
    email: str = Field(None, description="email Documentar")
    nome: str = Field(None, description="nome Documentar")
    data_nascimento: date = Field(
        None, description="data_nascimento Documentar"
    )
    active: bool = Field(None, description="active Documentar")
    escola_uuid: UUID = Field(None, description="escola_uuid Documentar")
    papel_uuid: UUID = Field(None, description="papel_uuid Documentar")
    escola_name: str = Field(None, description="escola_name Documentar")
    papel_name: str = Field(None, description="papel_name Documentar")
    access_level: int = Field(None, description="access_level Documentar")

    validate_senha = validator("senha", allow_reuse=True)(
        util.normalize_password
    )

    @model_validator(mode="before")
    def validators_user(self) -> "PostUsuario":
        try:
            if not "cpf" in self:
                raise error.CustomException(
                    422,
                    "É necessário informar o CPF para prosseguir.",
                )
            if models.Usuario.get("cpf", self["cpf"]):
                raise error.CustomException(
                    422,
                    f"'{self['CPF']}' já está cadastrado.",
                )
            if not "email" in self:
                raise error.CustomException(
                    422,
                    "É necessário informar o email para prosseguir.",
                )
            if models.Usuario.get("email", self["email"]):
                raise error.CustomException(
                    422,
                    f"'{self['email']}' já está cadastrado.",
                )
            False
            pass
            return self
        except Exception as e:
            raise error.custom_HTTPException(e)


class GetUsuario(BaseModel):
    """__summary__

    Attributes:
        cpf (str): descrever cpf.
        senha (str): descrever senha.
        email (str): descrever email.
        data_nascimento (date): descrever data_nascimento.
        active (bool): descrever active.
        escola_uuid (UUID): descrever escola_uuid.
        papel_uuid (UUID): descrever papel_uuid.
        escola_name (str): descrever escola_name.
        papel_name (str): descrever papel_name.
        access_level (str): descrever access_level.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """

    cpf: str | None = Field(None, description="cpf Documentar")
    email: str | None = Field(None, description="email Documentar")
    nome: str | None = Field(None, description="nome Documentar")
    data_nascimento: date | None = Field(
        None, description="data_nascimento Documentar"
    )
    active: bool | None = Field(None, description="active Documentar")
    escola_uuid: UUID | None = Field(
        None, description="escola_uuid Documentar"
    )
    papel_uuid: UUID | None = Field(None, description="papel_uuid Documentar")
    escola_name: str | None = Field(None, description="escola_name Documentar")
    papel_name: str | None = Field(None, description="papel_name Documentar")
    access_level: int | None = Field(
        None, description="access_level Documentar"
    )
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(
        None, description="updated_at Documentar"
    )

    class Config:
        from_attributes = True


class PutUsuario(BaseModel):
    """__summary__

    Attributes:
        cpf (str): descrever cpf.
        senha (str): descrever senha.
        email (str): descrever email.
        data_nascimento (date): descrever data_nascimento.
        active (bool): descrever active.
        escola_uuid (UUID): descrever escola_uuid.
        papel_uuid (UUID): descrever papel_uuid.
        escola_name (str): descrever escola_name.
        papel_name (str): descrever papel_name.
        access_level (str): descrever access_level.
    """

    cpf: str = Field(None, description="cpf Documentar")
    email: str = Field(None, description="email Documentar")
    nome: str | None = Field(None, description="nome Documentar")
    data_nascimento: date = Field(
        None, description="data_nascimento Documentar"
    )
    active: bool = Field(None, description="active Documentar")
    escola_uuid: UUID = Field(None, description="escola_uuid Documentar")
    papel_uuid: UUID = Field(None, description="papel_uuid Documentar")
    escola_name: str = Field(None, description="escola_name Documentar")
    papel_name: str = Field(None, description="papel_name Documentar")
    access_level: int = Field(None, description="access_level Documentar")
