def calculate_steps(array):
    steps = 0
    index = 0
    
    while index < len(array) and index >= 0:
        value = array[index]
        
        array[index] += 1
        
        index += value

        steps += 1

    return steps

def calculate_steps_part2(array):
    steps = 0
    index = 0
    
    while index < len(array) and index >= 0:
        value = array[index]
        
        if value >=  3:
            array[index] -= 1
        else:
            array[index] += 1
        
        index += value

        steps += 1

    return steps

def get_max(array):
    return array.index(max(array))
    # if len(array) == 1:
    #     return 0
    # if array[2] == 4:
    #     return 2
    # return 1

def get_count(array):
    result_dict = {}
    result = "".join(map(str, array))
    while result not in result_dict:
        # print(result_dict)
        result_dict[result] = 1
        max_value_index = get_max(array)
        max_value = array[max_value_index]
        array[max_value_index] = 0
        current_index = max_value_index + 1
        for _ in range(max_value):
            if (current_index >= len(array)):
                current_index = 0

            array[current_index] += 1
            current_index+=1
        
        result = "".join(map(str, array))

    return len(result_dict)



# 1 - Ler o input como array separado por \n
# 2 - Começar a leitura do array a partir de 0
# 3 - Enquanto o indice for menor que o tamanho do array e maior que 0
# 3.1 - Movimentar o indice baseado no valor lido
# 3.2 - Incrementar o indice lido em 1
# 3.3 - Incrementar no contador de passos
# 3.4 - Fim do laço
# 4 - Devolver o numero de passos



# ----- DAY 6


# 1 - Maior valor do array (empate pega o menor indice)
# 2 - A partir do proximo indice distribui um bloco para o seguinte bloco em ciclo
# 3 - Salvar o estado final apos distribuição em um dict
# 4 - Incrementar contador de ciclos de redistribuição

