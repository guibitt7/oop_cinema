from filmes import Filme
from clientes import Cliente
from salas import Sala
from filmes_web import FilmeWeb
import random

class Cinema:
    def __init__(self):
        self.salas_de_exibicao = []
        self.clientes = []
        self.salas = {}
        self.sala:Sala
        self._filme_web = FilmeWeb()
        self.filmes = []
        self.filme_sala_um = None
        self.filme_sala_dois = None
        self.clientes_sala_um = None
        self.clientes_sala_dois = None
        self._cod_sala_1 = '1'
        self._cod_sala_2 = '2'

        self.sala_1 = Sala(nome_sala=self._cod_sala_1)
        self.sala_2 = Sala(nome_sala=self._cod_sala_2)

    def instancia_clientes(self):
        self.clientes = [
            Cliente(nome = 'Fulano', cpf='300.224.660-37', sala=self._cod_sala_1),
            Cliente(nome = 'Beltrano', cpf='225.709.820-51', sala=self._cod_sala_1),
            Cliente(nome = 'Ciclano', cpf='542.159.460-26', sala=self._cod_sala_2),
            Cliente(nome = 'Alano', cpf='013.394.290-20', sala=self._cod_sala_1),
            Cliente(nome = 'Zutano', cpf='544.410.090-89', sala=self._cod_sala_2),
        ]

    def redirecionar_clientes_para_sala(self):
        for cliente in self.clientes:
            if cliente.sala not in self.salas:
                self.salas[cliente.sala] = Sala(nome_sala=cliente.sala)
            self.sala = self.salas[cliente.sala]
            self.sala.configurar_sala(self.sala.informacoes_filme, [cliente])

        self.clientes_sala_um = [cliente for cliente in self.clientes if cliente.sala == self._cod_sala_1]
        self.clientes_sala_dois = [cliente for cliente in self.clientes if cliente.sala == self._cod_sala_2]


    def instanciar_filme(self):
        filmes_mock = [
            {'Nome': 'O Poderoso Chefão', 'Diretor': 'Francis Ford Coppola'},
            {'Nome': 'Pulp Fiction: Tempo de Violência', 'Diretor': 'Quentin Tarantino'},
            {'Nome': 'A Origem', 'Diretor': 'Christopher Nolan'},
            {'Nome': 'O Senhor dos Anéis: A Sociedade do Anel', 'Diretor': 'Peter Jackson'}
        ]
        for informacoes_filme in filmes_mock:
            nome = informacoes_filme['Nome']
            diretor = informacoes_filme['Diretor']
            filme = Filme(nome=nome, diretor=diretor)
            self.filmes.append(filme)

    def sortear_filmes(self):
        filmes_sorteados = random.sample(self.filmes, 2)

        self.filme_sala_um = filmes_sorteados[0]
        self.filme_sala_dois = filmes_sorteados[1]

    def inserir_info_sala_um(self, informacoes_filme:Filme, lista_de_clientes:Cliente):
        self.sala_1.configurar_sala(informacoes_filme=informacoes_filme, clientes=lista_de_clientes)
        self.salas_de_exibicao.append(self.sala_1)

    def inserir_info_sala_dois(self, informacoes_filme:Filme, lista_de_clientes:Cliente):
        self.sala_2.configurar_sala(informacoes_filme=informacoes_filme, clientes=lista_de_clientes)
        self.salas_de_exibicao.append(self.sala_2)

    def exibir_detalhes_sala(self):
        for self.sala in self.salas_de_exibicao:
            self.sala.exibir_detalhes()