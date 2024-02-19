def tem_bomba_direita(board, position):
    if position + 1 >= len(board):
        return False
    if board[position+1] == "*":
        return True
    return False


def tem_bomba_esquerda(board, position):
    if position - 1 < 0:
        return False
    if board[position-1] == "*":
        return True
    return False


def conta_bombas(board, position):

    cont = 0
    if board[position] == "*":
        return -1

    if tem_bomba_direita(board, position):
        cont += 1

    if tem_bomba_esquerda(board, position):
        cont += 1

    return cont


def tem_bomba_acima(board, x, y):
    return True
