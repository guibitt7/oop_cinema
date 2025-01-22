import random

class Filme:

    def __init__(self, nome:str, diretor:str):
        self._nome = nome
        self._diretor = diretor

    @property
    def nome(self):
        return self._nome

    @property
    def diretor(self):
        return self._diretor
