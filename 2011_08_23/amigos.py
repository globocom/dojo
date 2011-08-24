import math


class Amigo(object):

    def __init__(self, id, latitude, longitude):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude


def amigos_proximos(amigos):
    dict_amigos={}
    for amigo in amigos:
        lista_amigos_proximos = []
        for outro_amigo in amigos:
            if outro_amigo[0] != amigo[0]:
                lista_amigos_proximos.append(
                    (
                        outro_amigo[0], 
                        distancia_entre_dois_pontos(amigo[1:], outro_amigo[1:])
                    )
                )
        lista_amigos_proximos = sorted(lista_amigos_proximos, cmp=lambda el1, el2: cmp(el1[1], el2[1]))
        lista_amigos_proximos = [outro_amigo[0] for outro_amigo in lista_amigos_proximos]
        dict_amigos[amigo[0]] = lista_amigos_proximos
    return dict_amigos


def distancia_entre_dois_pontos(ponto1, ponto2):
    return math.sqrt((ponto2[0] - ponto1[0]) ** 2 + (ponto2[1] - ponto1[1]) ** 2)
