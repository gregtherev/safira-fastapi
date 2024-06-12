from typing import List, Optional
from schemas.schemas import PetSchema, UserSchema
from data.mock_data import mocked_pets, mocked_users
from models.models import Pet, User


class UserAdapter:
    def get_all_users(self) -> List[UserSchema]:
        return [UserSchema.model_validate(user) for user in mocked_users]

    def get_user(self, user_id: int) -> Optional[UserSchema]:
        for user in mocked_users:
            if user_id == user.id:
                return UserSchema.model_validate(user)
        return None

    def create_user(self, user_schema: UserSchema) -> UserSchema:
        user = User(**user_schema.model_dump())
        mocked_users.append(user)
        return UserSchema.model_validate(user)


class PetAdapter:
    def get_all_pets(self) -> Optional[List[PetSchema]]:
        return [PetSchema.model_validate(pet) for pet in mocked_pets]

    def get_pet(self, pet_id: int) -> Optional[List[PetSchema]]:
        for pet in mocked_pets:
            if pet_id == pet.id_dono:
                return PetSchema.model_validate(pet)
        return None

    def create_pet(self, pet_schema: PetSchema) -> Optional[PetSchema]:
        pet = Pet(**pet_schema.model_dump())
        mocked_pets.append(pet)
        return PetSchema.model_validate(pet)
