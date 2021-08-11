def main():
    return True



def unidade(num):
    UNIDADES = {
        0: '',
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
    }
    return UNIDADES[num]

def dezena(num):
    DEZENAS = {
        0: '',
        1: 'X',
        2: 'XX',
        3: 'XXX',
        4: 'XL',
        5: 'L',
        6: 'LX',
        7: 'LXX',
        8: 'LXXX',
        9: 'XC',
    }
    return DEZENAS[num]

def centena(num):

    CENTENAS = {
        0: '',
        1: 'C',
        2: 'CC',
        3: 'CCC',
        4: 'CD',
        5: 'D',
        6: 'DC',
        7: 'DCC',
        8: 'DCCC',
        9: 'CM',
    }
    return CENTENAS[num]

def milhares(num):
    MILHARES = {
        0: '',
        1: 'M',
        2: 'MM',
        3: 'MMM',
    }
    return MILHARES[num]


def solver(num):
    ans = ""
    ans = ans + milhares(num//1000)
    ans = ans + centena(num%1000//100)
    ans = ans + dezena(num%100//10)
    ans = ans + unidade(num%10)
    return ans


# "leonardo"
# "tcarreira"
# "Lara"