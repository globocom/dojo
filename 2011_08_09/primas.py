import math

def valor_da_letra(letra):
    if letra.islower():
        return ord(letra)-ord('a')+1
    else:
        return ord(letra)-ord('A')+27

def valor_da_palavra(palavra):
    return sum([valor_da_letra(letra) for letra in palavra])

def eh_primo(numero):
    if numero == 1:
        return False
    for n in xrange(2, int(math.sqrt(numero)) + 1):
        if numero % n == 0:
            return False
    return True

def palavra_eh_prima(palavra):
    valor = valor_da_palavra(palavra)
    return eh_primo(valor)
