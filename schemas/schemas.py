from pydantic import BaseModel, ConfigDict
from typing import List


class PetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    nome: str
    especie: str
    id_dono: int


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    model_config    
    id: int
    nome: str
    email: str
    animais: List[PetSchema] = []
