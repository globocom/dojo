def get_first_diag_points(matriz):
	colunas = len(matriz[0])
	linhas = len(matriz)
	
	posicoes = []

	for i in range(0, colunas):
		posicoes.append((0, i))

	for j in range(1, linhas):
		posicoes.append((j, 0))

	return sorted(posicoes)

