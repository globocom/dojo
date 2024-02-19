def main(palavra):
    letra_atual = None
    letra_max = None
    count_atual = 0
    count_max = 0

    for i, letra in enumerate(palavra):
        letra_atual = letra
        if i == 0:
            letra_max = letra
            count_atual = 1
            count_max = 1
            continue

        if letra_atual == palavra[i - 1]:
            count_atual += 1
        else:
            count_max = count_atual
            count_atual = 1
            continue

        if count_atual > count_max:
            letra_atual = letra
            letra_max = letra_atual
            count_max = count_atual

    return letra_max * count_max
