import math

def pinta_fita(fita):
    fita_final = [ x for x in fita ]
    for i, v in enumerate(fita):
        if v:
            if i > 0: 
                fita_final[i-1] = 1 
            if i < len(fita) - 1:
                fita_final[i+1] = 1

    return fita_final


def criar_fita(tamanho, coords):
    fita = [0] * tamanho
    for valor in coords:
        fita[valor - 1] = 1
    return fita

def main(tamanho, coords):
    n = len(coords)
    diff = [math.ceil((coords[i + 1] - coords[i]) / 2) for i in range(n - 1)]
    diff = [coords[0]-1 , *diff , (tamanho - coords[-1])]
    print(diff)
    return max(diff)