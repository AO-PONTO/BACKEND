from datetime import datetime, time, date
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, validator, model_validator

from app import error, models, util




__all__ = [
    "PostTurmas",
    "GetTurmas",
    "PutTurmas",
]

class HorarioSchema(BaseModel):
    dia: int
    hora: str

class PostTurmas(BaseModel):
    """__summary__

    Attributes:
        disciplina (str): descrever disciplina.
        sala (UUID): descrever sala.
        nome_professor (str): descrever nome_professor.
        turno (str): descrever turno.
        horario (time): descrever horario.
        ano (date): descrever ano.
    """
    
    disciplina: str = Field(None, description="disciplina Documentar")
    sala: UUID = Field(None, description="sala Documentar")
    nome_professor: str = Field(None, description="usuário do tipo professor")
    horario: list[HorarioSchema] | str = Field(description="horario Documentar")
    
    #     validate_disciplina= validator("disciplina", allow_reuse=True)(...)
    #     validate_sala= validator("sala", allow_reuse=True)(...)
    #     validate_nome_professor= validator("nome_professor", allow_reuse=True)(...)
    #     validate_turno= validator("turno", allow_reuse=True)(...)
    #     validate_horario= validator("horario", allow_reuse=True)(...)
    #     validate_ano= validator("ano", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_PostLocation(self) -> "PostTurmas":
        try:
            if not "horario" in self:
                raise error.CustomException(
                    422,
                    "É necessário informar o horario para prosseguir.",
                )
            self["horario"] = str(self["horario"])
            return self
        except Exception as e:
            raise error.custom_HTTPException(e)



class GetTurmas(BaseModel):
    """__summary__

    Attributes:
        disciplina (str): descrever disciplina.
        sala (UUID): descrever sala.
        nome_professor (str): descrever nome_professor.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """
    
    disciplina: str | None = Field(None, description="disciplina Documentar")
    sala: UUID | None = Field(None, description="sala Documentar")
    nome_professor: str | None = Field(None, description="usuário do tipo professor")
    horario: str | None = Field(None, description="horario Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(None, description="updated_at Documentar")
    
    class Config:
        from_attributes = True


class PutTurmas(BaseModel):
    """__summary__

    Attributes:
        disciplina (str): descrever disciplina.
        sala (UUID): descrever sala.
        nome_professor (str): descrever nome_professor.
        ano (date): descrever ano.
    """
    
    disciplina: str = Field(None, description="disciplina Documentar")
    sala: UUID = Field(None, description="sala Documentar")
    nome_professor: str = Field(None, description="usuário do tipo professor")
    horario: str = Field(None, description="horario Documentar")