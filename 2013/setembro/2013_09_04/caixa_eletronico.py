NOTAS_DISPONIVEIS = [100, 50, 20, 10]

def sacar(valor):
	restante = valor
	notas = {}
	for nota in NOTAS_DISPONIVEIS:
		while restante >= nota:
			restante = restante - nota
			notas[nota] = notas.get(nota, 0) + 1
	
	if restante > 0:
		raise Exception("valor indisponivel")

	return notas


def imprime_sacar(valor):
	saida = sacar(valor)
	mensagem = ""
	for valor, quantidade in reversed(saida.items()):
		if mensagem:
			mensagem += " e "
		else:
			mensagem = "Entregar "
		mensagem += "%1s nota de R$%2s,00" % (quantidade, valor)
	return mensagem

