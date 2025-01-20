class Cliente:

    def __init__(self):
        self.cliente_sala_um = []
        self.cliente_sala_dois = []

    def redirecionar_clientes_p_sala(self):
        clientes = [
                {'Nome': 'Fulano', 'CPF': '300.224.660-37', 'Sala': '1'},
                {'Nome': 'Beltrano', 'CPF': '225.709.820-51', 'Sala': '1'},
                {'Nome': 'Cicrano', 'CPF': '542.159.460-26', 'Sala': '2'},
                {'Nome': 'Alano', 'CPF': '013.394.290-20', 'Sala': '1'},
                {'Nome': 'Zutano', 'CPF': '544.410.090-89', 'Sala': '2'},
                ]

        for cliente in clientes:
            if cliente['Sala'] == '1':
                self.cliente_sala_um.append(cliente)
            else:
                self.cliente_sala_dois.append(cliente)

