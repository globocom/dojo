def main(matriz, coluna):
	aux = 0
	for i in range(len(matriz)):
		if not (i + 1) >=  len(matriz):
			value = matriz[i][coluna]
			prox = matriz[i+1][coluna]
			if value > prox:
				aux = matriz[i+1]
				matriz[i+1] = matriz[i]
				matriz[i] = aux

	return matriz

# for i in range(tamanho):
# for index, line in enumerate(matriz)

