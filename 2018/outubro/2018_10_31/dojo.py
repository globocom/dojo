def next_position(matriz, posicao):
    direction = [(0,1),(1,0)]
    for d in direction:
        new_cor = posicao + d
        try:
            if matriz[new_cor[0]][new_cor[1]] is None:
                return  new_cor
        except:
            continue

def main(linha, coluna):
    lista = [
        [None for i in range(coluna)]
        for i in range(linha)
    ]
    count = 1
    x=0
    y=0
    # dir=
    for l in range(linha):
        for c in range(coluna):
            lista[l][c] = count
            count += 1
    return lista



    # if(coluna == 1):
    #     return [[1]]
    # return[[1, 2]]
