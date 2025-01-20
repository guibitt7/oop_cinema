import random

class Filmes:

    def __init__(self):
        self._filmes =  [
            {'nome': 'Sonic 3', 'diretor': 'Jeff Fowler'},
            {'nome': 'Mufasa: O Rei Leão', 'diretor': 'Barry Jenkins'},
            {'nome': 'O Auto da Compadecida', 'diretor': 'Guel Arraes'},
            {'nome': 'Chico Bento e a Goiabeira Maravilhosa', 'diretor': 'Fernanda Fraiha'}
            ]
        self.filme_sala_um = []
        self.filme_sala_dois = []

    def sortear_filmes(self):
         filmes_sorteados = random.sample(self._filmes, 2)

         self.filme_sala_um = filmes_sorteados[0]
         self.filme_sala_dois = filmes_sorteados[1]

