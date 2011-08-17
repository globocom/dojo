def fizz_ou_buzz(numero):
    retorno = ""

    if numero % 3 == 0:
        retorno += "fizz"

    if numero % 5 == 0:
        retorno += "buzz"

    if retorno:
        return retorno

    return str(numero)
    
def fizz_buzz(numeros):
    return '\n'.join([fizz_ou_buzz(numero) for numero in numeros])