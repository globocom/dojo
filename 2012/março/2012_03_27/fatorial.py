def fatorial(numero, base):
    resultado = 1
    while numero > 0:
        resultado *= numero
        numero -= base
    return resultado
