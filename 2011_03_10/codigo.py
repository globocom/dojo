# coding: utf-8

def preencha_cheque(valor):

    numeros = {
                1: 'um',
                2: 'dois',
                3: 'três',
                4: 'quatro',
                5: 'cinco',
                6: 'seis',
                7: 'sete', 
                8: 'oito', 
                9: 'nove',
                10: 'dez',
                11: 'onze',
                12: 'doze',
                13: 'treze',
                14: 'catorze',
                15: 'quinze',
                16: 'dezesseis',
                17: 'dezessete',
                18: 'dezoito',
                19: 'dezenove',
                20: 'vinte',
                30: 'trinta'
    }
    
    if valor < 1:
        return 'cinquenta centavos'
    
    if valor == 1.00:                 
        sufixo = "real"
    elif valor > 1.00:
        sufixo = "reais"
        
    valores = []
    
    if valor <= 20:
        valores.append(numeros[int(valor)])
    else:
        valores.append(numeros[int(valor) / 10 * 10])
        if int(valor) % 10:
            valores.append(numeros[int(valor) % 10])
    
    return " e ".join(valores)+ " " + sufixo
