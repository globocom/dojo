# 'ABC' -> 2
# 'DEF' -> 3
# 'GHI' -> 4
# 'JKL' -> 5
# 'MNO' -> 6
# 'PQRS' -> 7
# 'TUV' -> 8
# 'WXYZ' -> 9
# Espaço -> 0
# Espera -> _


def words(phrase):
    result = ""
    for l in phrase:
        if len(result) and letter(l)[0] == result[-1]:
            result += '_'
        result += letter(l)
    return result


def letter(char):
    dicio = {
        'ABC': '2',
        'DEF': '3',
        'GHI': '4',
        'JKL': '5',
        'MNO': '6',
        'PQRS': '7',
        'TUV': '8',
        'WXYZ': '9',
        ' ': '0'
    }

    for k, v in dicio.items():
        if char in k:
            return letter_position(k, char) * v

    return None


def letter_position(letterSet, letter):
    try:
        return letterSet.index(letter) + 1
    except ValueError:
        return 0
