import random

class Filme:

    def __init__(self, nome, diretor):
        self.filmes =  [
            {'nome': 'Sonic 3', 'diretor': 'Jeff Fowler'},
            {'nome': 'Mufasa: O Rei Leão', 'diretor': 'Barry Jenkins'},
            {'nome': 'O Auto da Compadecida', 'diretor': 'Guel Arraes'},
            {'nome': 'Chico Bento e a Goiabeira Maravilhosa', 'diretor': 'Fernanda Fraiha'}
            ]
        self.nome = nome
        self.diretor = diretor
