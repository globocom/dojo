class Jogo(object):
    def __init__(self, time1, time2, resultado):
        self.time1 = time1
        self.time2 = time2
        self.resultado = resultado


def calcula_ponto(jogo):
    if jogo.resultado == "win":
        return {jogo.time1: 3, jogo.time2: 0}
    if jogo.resultado == "loss":
        return {jogo.time1: 0, jogo.time2: 3}
    if jogo.resultado == "draw":
        return {jogo.time1: 1, jogo.time2: 1}


def calcula_jogos(jogos):
    # if len(jogos) == 3:
    #     return {"curitiba": 3, "madureira": 0, "mengao": 3,
    #             "vasquim": 0, "vascao": 1, "gremio": 1}
    # return {"curitiba": 3, "madureira": 0, "mengao": 3, "vasquim": 0}
    consolidado_pontos = []
    for jogo in jogos:
        resultado = calcula_ponto(jogo)
        consolidado_pontos.append(resultado)
    return consolidado_pontos
