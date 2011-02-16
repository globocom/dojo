def wrap(palavras, colunas):
    if len(palavras) < colunas:
        return palavras
    i = 0
    resultado = []
    for palavra in palavras.split():
        i += len(palavra)
        if len(resultado) > 0:
            if i < colunas:
                resultado.append(' ')
                resultado.append(palavra)
                i += 1
            else:
                resultado.append('\n')
                resultado.append(palavra)
                i = 0
        else:
            resultado.append(palavra)
            
    return ''.join(resultado)