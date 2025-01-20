class Poltrona:
    def __init__(self, id, cor):
        self._id = id
        self._cor = cor
        self._esta_ocupada = False
        self._cliente_atual = None

    def ocupar(self, cliente):
        if not self._esta_ocupada:
            self._esta_ocupada = True
            self._cliente_atual = cliente
            return True
        return False

    def __str__(self):
        if self._esta_ocupada:
            return f"Poltrona {self._id} - Cor: {self._cor} - Ocupada por {self._cliente_atual['Nome']}"
        else:
            return f"Poltrona {self._id} - Cor: {self._cor} - Disponível"

    @staticmethod
    def criar_poltronas():
        cores = ['Vermelha', 'Azul', 'Verde', 'Preta', 'Branca']
        poltronas = []
        for i in range(5):
            poltrona = Poltrona(id=f'P{i + 1}', cor=cores[i])
            poltronas.append(poltrona)
        return poltronas

