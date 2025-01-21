from filmes import Filme
from clientes import Cliente
from salas import Sala
import random

class Cinema:
    def __init__(self):
        self.salas_de_exibicao = []
        self.clientes = []
        self.salas = {}
        self.filmes = []
        self.filme_sala_um = None
        self.filme_sala_dois = None


    def _estanciar_clientes(self):
        self.clientes = [
            Cliente(nome='Fulano', cpf='300.224.660-37', sala='1'),
            Cliente(nome='Beltrano', cpf='225.709.820-51', sala='1'),
            Cliente(nome='Cicrano', cpf='542.159.460-26', sala='2'),
            Cliente(nome='Alano', cpf='013.394.290-20', sala='1'),
            Cliente(nome='Zutano', cpf='544.410.090-89', sala='2')
        ]

    def _redirecionar_clientes_para_salas(self):
        for cliente in self.clientes:
            if cliente.sala not in self.salas:
                self.salas[cliente.sala] = Sala(nome_sala=cliente.sala)
            sala = self.salas[cliente.sala]
            sala.configurar_sala(sala.informacoes_filme, [cliente])

        self.clientes_sala_um = [cliente for cliente in self.clientes if cliente.sala == '1']
        self.clientes_sala_dois = [cliente for cliente in self.clientes if cliente.sala == '2']


    def _instanciar_filme(self):
        self.filmes = [
            Filme(nome='Sonic 1', diretor='De teste1'),
            Filme(nome='Sonic 2', diretor='De teste2'),
            Filme(nome='Sonic 3', diretor='De teste3'),
            Filme(nome='Sonic 4', diretor='De teste4')
        ]

    def _sortear_filmes(self):
         filmes_sorteados = random.sample(self.filmes, 2)

         self.filme_sala_um = filmes_sorteados[0]
         self.filme_sala_dois = filmes_sorteados[1]

    def _criar_sala(self, nome_da_sala, informacoes_filme, lista_de_clientes):
        sala = Sala(nome_da_sala)
        sala.configurar_sala(informacoes_filme, lista_de_clientes)
        self.salas_de_exibicao.append(sala)

    def executar(self):
        self._estanciar_clientes()
        self._instanciar_filme()
        self._sortear_filmes()
        self._redirecionar_clientes_para_salas()

        self._criar_sala("1", self.filme_sala_um, self.clientes_sala_um)
        self._criar_sala("2", self.filme_sala_dois, self.clientes_sala_dois)

    def exibir_detalhes(self):
        for sala in self.salas_de_exibicao:
            sala.exibir_detalhes()

