def main(elementos, valor):
    soma = 0
    while soma < valor:
        soma += elementos[0]

    if soma == valor:
        return [[elementos[0]] * int(soma / elementos[0])]

    soma = 0
    while soma < valor:
        soma += elementos[1]

    if soma == valor:
        return [[elementos[1]] * int(soma / elementos[1])]

    soma = 0
    recursivo(elementos, [], valor)
    return lista_global

lista_global =[]
def recursivo(elementos, resultado, valor):
    if (sum(resultado) > valor):
        return

    if (sum(resultado) == valor):
        lista_global.append(resultado)
        return


    recursivo(elementos, resultado + [elementos[0]],  valor)
    if len(elementos) > 1:
        recursivo(elementos[1:], resultado,  valor)

#    if valor in elementos:
#        return [[valor]]



#    return [elementos]
