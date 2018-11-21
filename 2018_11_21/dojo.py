def start_lampadas(lampadas):
    return ["off"]*lampadas


def is_divisible(num, div):
    return num % div == 0


def switch_lampada(lampada):
    return "on" if lampada == "off" else "off"


def percorre_corredor(lampadas, indice):
    aux = []
    for posicao, lampada in enumerate(lampadas):
        if is_divisible(posicao+1, indice):
            aux.append(switch_lampada(lampada))
        else:
            aux.append(lampada)
    return aux


def main(l):
    init = start_lampadas(l)
    for i in range(l):
        init = percorre_corredor(init, i+1)
    return init
