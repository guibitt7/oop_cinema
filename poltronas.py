from clientes import Cliente


class Poltrona:
    def __init__(self, id, cor:str):
        self._id = id
        self._cor = cor
        self._esta_ocupada = False
        self._cliente_atual:Cliente = None

    def ocupar(self, cliente:Cliente):
        if not self._esta_ocupada:
            self._esta_ocupada = True
            self._cliente_atual = cliente
            return True
        return False

    def __str__(self):
        if self._esta_ocupada:
            return f"Poltrona {self._id} - Cor: {self._cor} - Ocupada por {self._cliente_atual.nome}"
        else:
            return f"Poltrona {self._id} - Cor: {self._cor} - Disponível"


    @property
    def id(self):
        return self._id
    @property
    def cor(self):
        return self._cor
    @property
    def esta_ocupada(self):
        return self._esta_ocupada
    @property
    def cliente_atual(self):
        return self._cliente_atual