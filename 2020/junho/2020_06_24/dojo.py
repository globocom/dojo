def result(valor, nota):
	resto = valor % nota
	qtd = valor // nota
	return (resto, qtd)

def main(valor):
	notas = [100,50,20,10]

	resultado = valor
	resposta = []
	for nota in notas:
		resultado, quantidade = result(resultado, nota)
		if quantidade > 0:
			resposta.append((nota, quantidade))
	return resposta		
	
