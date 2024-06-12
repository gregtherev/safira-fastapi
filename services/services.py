from fastapi import HTTPException
from typing import List, Optional

from adapters.adapter import PetAdapter, UserAdapter 
from schemas.schemas import PetSchema, UserSchema


class PetService():
    def __init__(self):
        self.adapter = PetAdapter()

    def get_all_pets(self) -> Optional[List[PetSchema]]:
        return self.adapter.get_all_pets()

    def get_pet(self, pet_id: int) -> Optional[PetSchema]:
        pet = self.adapter.get_pet(pet_id)
        if pet is None:
            raise HTTPException(status_code=404,
                                detail="Animal não encontrado")
        return pet

    def create_pet(self, pet_schema: PetSchema) -> PetSchema:
        return self.adapter.create_pet(pet_schema)


class UserService():
    def __init__(self):
        self.adapter = UserAdapter()

    def get_all_users(self) -> List[UserSchema]:
        return self.adapter.get_all_users()

    def get_user(self, user_id: int) -> Optional[UserSchema]:
        user = self.adapter.get_user(user_id)
        if user is None:
            raise HTTPException(status_code=404,
                                detail="Usuário não encontrado")
        return user

    def create_user(self, user: UserSchema) -> UserSchema:
        return self.adapter.create_user(user)
