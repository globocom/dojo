import string

def encotel(frase):
	teclado = {
			'abc' : '2',
			'def' : '3',
			'ghi': '4',
			'jkl': '5',
	 		'mno' : '6',
			'pqrs' : '7',
			'tuv' : '8',
			'wxyz' : '9',
	}
	
	numeros = []
	for letra in frase:
		if letra not in string.letters:
			numeros.append(letra)
			continue

		numeros.extend([teclado[chave] for chave in teclado.keys() if letra in chave])

	return "".join(numeros)