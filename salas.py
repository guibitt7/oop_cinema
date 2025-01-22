from poltronas import Poltrona
from filmes import Filme
from clientes import Cliente

class Sala:
    def __init__(self, nome_sala):
        self.nome_sala:str = nome_sala
        self.informacoes_filme:Filme = None
        self._poltronas:list[Poltrona] = []
        self._criar_poltronas(5)
        self._cliente = Cliente(nome=None, cpf=None, sala=None)
        self._poltrona = Poltrona(id=None, cor=None)

    def configurar_sala(self, informacoes_filme:Filme, clientes:Cliente):
        self.informacoes_filme = informacoes_filme

        if len(clientes) > len(self._poltronas):
            print(f"A sala {self.nome_sala} está cheia. Não é possível acomodar mais de {len(self._poltronas)} pessoas.")
            clientes = clientes[:len(self._poltronas)]

        for i, cliente in enumerate(clientes):
            self._poltronas[i].ocupar(cliente)

    def exibir_detalhes(self):
        print(f"Sala: {self.nome_sala}")
        print(f"Filme em exibição: {self.informacoes_filme.nome} - Diretor: {self.informacoes_filme.diretor}")
        print("\nPoltronas na sala:")
        for poltrona in self._poltronas:
            print(poltrona)

    def _criar_poltronas(self, quantidade=5):
        cores = ['Vermelho', 'Azul', 'Verde', 'Preto', 'Branca']
        for i in range(quantidade):
            poltorna = Poltrona(id=f'{i +1}', cor=cores[i])
            self._poltronas.append(poltorna)

    @property
    def poltronas(self):
        return self._poltronas

