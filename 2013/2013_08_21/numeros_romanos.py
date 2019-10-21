LETRAS_ROMANAS = {
  "Y": 0,
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000
}

def romano_para_decimal(romano):
    resposta = 0
    romano = romano + 'Y'
    if (len(romano) == 1):
        return LETRAS_ROMANAS[romano]

    for i in xrange(len(romano) - 1 ):
        atual = LETRAS_ROMANAS[romano[i]]
        prox = LETRAS_ROMANAS[romano[i + 1]]

        if atual < prox:
            resposta -= atual
        else:
            resposta += atual
    return resposta
    