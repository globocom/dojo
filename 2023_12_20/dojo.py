
# 1 - ler a lista de linhas, para cada linha:
# 1.1 - percorrer a linha e validar o tipo do caracter lido
# 1.2 - se for tipo numerico e for o primeiro a ser lido
# 1.2.1 - salvar na variavel auxiliar, multiplicando por 10
# 1.3 - se for tipo numero e for o ultimo a ser lido
# 1.3.1 - somar na variavel auxiliar
# 2 - retornar a variavel auxiliar

# Rapha
# Pedro
# Fernanda
# Syl
# Juan


def main():
    return True

def calculate_document(lines):
    aux1 = 0
    for line in lines:
        first = found_first_number(line) * 10
        second = found_first_number(line[::-1])
        aux1 += first + second
    return aux1

def calculate_document_2(lines):
    aux1 = 0
    for line in lines:
        first = found_first_number_2(line) * 10
        second = found_first_number_2(line[::-1], True)
        aux1 += first + second
    return aux1

def found_first_number_2(line, reverse=False):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    letters = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    letters_reverse = {
        "eno": 1,
        "owt": 2,
        "eerht": 3,
        "ruof": 4,
        "evif": 5,
        "xis": 6,
        "neves": 7,
        "thgie": 8,
        "enin": 9
    }

    l_list = letters_reverse if reverse else letters

    less = len(line)
    value_less = ""
    for num in l_list:
        index = line.find(num)
        if index > -1 and index < less:
            less = index
            value_less = num
    
    for index, c in enumerate(line):
        if index < less and c in numbers:
            return int(c)
    
    return l_list[value_less] or 0

    # letters_reverse = {
    #     "eno": 1,
    #     "owt": 2,
    #     "eerht": 3,
    #     "ruof": 4,
    #     "evif": 5,
    #     "xis": 6,
    #     "neves": 7,
    #     "thgie": 8,
    #     "enin": 9
    # }
    # for c in line:
    #     if c in numbers:
    #         return int(c)
    # return -1


def found_first_number(line):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for c in line:
        if c in numbers:
            return int(c)
    return -1
