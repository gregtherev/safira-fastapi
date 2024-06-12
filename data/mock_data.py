from models.models import User, Pet


mocked_pets = [
    Pet(id=1, nome="Totó", especie="Cachorro", id_dono=1),
    Pet(id=2, nome="Miau", especie="Gato", id_dono=1),
    Pet(id=3, nome="Pru", especie="Pomba", id_dono=2)
]


mocked_users = [
    User(id=1, nome="Fulano da Silva", email="email@email.com", animais=[mocked_pets[0], mocked_pets[1]]), # noqa
    User(id=2, nome="Ciclana Junior", email="anotheremail@email.com", animais=[mocked_pets[-1]]) # noqa
]


# mocked_users = []
# mocked_pets = {}
