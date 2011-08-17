import math
import string


def eh_prima(palavra):
	return eh_numero_primo(sum(string.ascii_letters.find(letra) + 1 for letra in palavra))
	
def eh_numero_primo(numero):
	
	if numero <= 1:
		return False
	
	for i in range(2, int(math.sqrt(numero) + 1)):
		if numero % i == 0:
			return False
	
	return True