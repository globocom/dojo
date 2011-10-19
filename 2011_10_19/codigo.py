def menor_numero_divisivel(num_limite):
    achei_o_numero = False
    contador = num_limite
    while not achei_o_numero:
        for i in range(num_limite, 0, -1):
            achei_o_numero = contador % i == 0
            if not achei_o_numero:
                break

        contador += num_limite

    return contador - num_limite
