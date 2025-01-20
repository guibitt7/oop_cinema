from cinema import Cinema

cinema = Cinema()

cinema.gerenciador_de_filmes.sortear_filmes()
cinema.gerenciador_de_clientes.redirecionar_clientes_p_sala()

cinema.criar_sala("1", cinema.gerenciador_de_filmes.filme_sala_um, cinema.gerenciador_de_clientes.cliente_sala_um)
cinema.criar_sala("2", cinema.gerenciador_de_filmes.filme_sala_dois, cinema.gerenciador_de_clientes.cliente_sala_dois)

cinema.exibir_detalhes()
