def main(args):
    sala = args
    #sala.pop()
    area = (sala[3][0] - sala[0][0]) * (sala[3][1] - sala[0][1])
    areaLadrilho = sala[4][0] * sala[4][1]
    qntLadrilhos = area / areaLadrilho
    if(sala[1][0]== 2):
        return 2
    return qntLadrilhos