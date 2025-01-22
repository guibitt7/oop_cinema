from cinema import Cinema
from criar_csv import CSV


cinema = Cinema()
gerador_csv = CSV(filename="cinema_info.csv")


cinema.instancia_clientes()
cinema.instanciar_filme()

cinema.sortear_filmes()
cinema.redirecionar_clientes_para_sala()

info_filme_1 = cinema.filme_sala_um
info_filme_2 = cinema.filme_sala_dois
info_clientes_1 = cinema.clientes_sala_um
info_clientes_2 = cinema.clientes_sala_dois

cinema.inserir_info_sala_um(info_filme_1, info_clientes_1)
cinema.inserir_info_sala_dois(info_filme_2, info_clientes_2)

cinema.exibir_detalhes_sala()

gerador_csv.gerar_csv(cinema.salas_de_exibicao)
