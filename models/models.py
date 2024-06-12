from typing import List


class Pet:
    def __init__(self, id: int, nome: str, especie: str, id_dono: int):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.id_dono = id_dono


class User:
    def __init__(self, id: int, nome: str, email: str, animais: List[Pet]):
        self.id = id
        self.nome = nome
        self.email = email
        self.animais = animais or []
