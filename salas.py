from poltronas import Poltrona

class Sala:
    def __init__(self, nome_sala):
        self.nome_sala = nome_sala
        self.informacoes_filme = None
        self._poltronas = []

    def configurar_sala(self, informacoes_filme, clientes):
        self.informacoes_filme = informacoes_filme
        self._poltronas = Poltrona.criar_poltronas()

        if len(clientes) > len(self._poltronas):
            print(f"A sala {self.nome_sala} está cheia. Não é possível acomodar mais de {len(self._poltronas)} pessoas.")
            clientes = clientes[:len(self._poltronas)]

        for i, cliente in enumerate(clientes):
            self._poltronas[i].ocupar(cliente)

    def exibir_detalhes(self):
        print(f"Sala: {self.nome_sala}")
        print(f"Filme em exibição: {self.informacoes_filme['nome']} - Diretor: {self.informacoes_filme['diretor']}")
        print("\nPoltronas na sala:")
        for poltrona in self._poltronas:
            print(poltrona)
