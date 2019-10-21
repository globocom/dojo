
def expressao_matematica(expressao):
        
    index = expressao.find('+')
    
    if index > 0:
        valor = expressao[:index]
        return expressao_matematica(valor) + expressao_matematica(expressao[index+1:])
        
    index = expressao.rfind('-')
    
    if index > 0:
        valor = expressao[:index]
        return expressao_matematica(valor) - expressao_matematica(expressao[index+1:])
        
    index = expressao.find('*')
    
    if index > 0:
        valor = expressao[:index]
        return expressao_matematica(valor) * expressao_matematica(expressao[index+1:])
        
    return int(expressao)