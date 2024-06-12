from fastapi import FastAPI

from schemas.schemas import PetSchema, UserSchema 
from services.services import PetService, UserService

app = FastAPI()

pet_service = PetService()
user_service = UserService()


@app.get("/pets", summary="Listar todos animais")
def get_pets():
    return pet_service.get_all_pets()


@app.get("/pets/{pet_id}", summary="Buscar um animal")
def find_pet(pet_id: int):
    return pet_service.get_pet(pet_id)


@app.post("/pets", summary="Criar um animal")
def create_pet(pet_schema: PetSchema):
    return pet_service.create_pet(pet_schema)


@app.get("/users", summary="Listar todos usuários")
def get_users():
    return user_service.get_all_users()


@app.get("/users/{user_id}", summary="Buscar um usuário")
def find_user(user_id: int):
    return user_service.get_user(user_id)


@app.post("/users", summary="Criar um usuário")
def create_user(user_schema: UserSchema):
    return user_service.create_user(user_schema)
