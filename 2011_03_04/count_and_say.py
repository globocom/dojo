def count_and_say(palavra):
    dicionario = {}
    palavra = palavra.replace(' ', '')
    for letra in palavra:
        if not letra in dicionario.keys():
            dicionario[letra] = 1
        else:
            dicionario[letra] += 1
            
    retorno = ''
    
    for letra, quantidade in dicionario.items():
        retorno += '%d %s ' % (quantidade, letra)
    return retorno.rstrip()
    