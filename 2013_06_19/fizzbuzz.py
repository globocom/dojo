
def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'FizzBuzz'
    if numero % 3 == 0:
        return 'Fizz'
    if numero % 5 == 0:
        return 'Buzz'
    return numero

def fizzbuzz_lista(lista):
    resultado = []
    for numero in lista:
        resultado.append(fizzbuzz(numero))
    return resultado