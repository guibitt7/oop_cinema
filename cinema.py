from filmes import Filmes
from clientes import Cliente
from salas import Sala

class Cinema:
    def __init__(self):
        self.salas_de_exibicao = []
        self.gerenciador_de_filmes = Filmes()
        self.gerenciador_de_clientes = Cliente()

    def criar_sala(self, nome_da_sala, informacoes_filme, lista_de_clientes):
        sala = Sala(nome_da_sala)
        sala.configurar_sala(informacoes_filme, lista_de_clientes)
        self.salas_de_exibicao.append(sala)

    def exibir_detalhes(self):
        for sala in self.salas_de_exibicao:
            sala.exibir_detalhes()

