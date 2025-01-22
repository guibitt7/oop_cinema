import pandas as pd

class CSV:
    def __init__(self, filename):
        self._filename = filename
        self._relatorio_cinema:pd.DataFrame

    def gerar_csv(self, salas):
        data = []
        for sala in salas:
            for poltrona in sala.poltronas:
                if poltrona.esta_ocupada:
                    cliente = poltrona.cliente_atual
                    data.append({
                        "Nome do Cliente": cliente.nome,
                        "Sala Escolhida": sala.nome_sala,
                        "Código da Poltrona": poltrona.id,
                        "Nome do Filme": sala.informacoes_filme.nome,
                        "Diretor do Filme": sala.informacoes_filme.diretor,
                    })
        
        self._relatorio_cinema = pd.DataFrame(data)

        try:
            self._relatorio_cinema.to_csv(self._filename, sep=';', index=False, encoding="utf-8", mode='w')
            print(f"Arquivo CSV '{self._filename}' gerado com sucesso!")
        except IOError as e:
            print(f"Erro ao gerar o arquivo CSV: {e}")
