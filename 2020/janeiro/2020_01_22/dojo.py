def roman_to_int(roman):
    letras = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    return letras[roman]


def get_numbers(roman):
    values = []
    for value in roman:
        values.append(roman_to_int(value))
    return values


def calc(numbers):
    result = 0
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            result += numbers[i]
        else:
            if numbers[i] >= numbers[i + 1]:
                result += numbers[i]
            else:
                result -= numbers[i]

    return result

    # if len(numbers) == 3:
    #     return 7
    # elif numbers[0] == 1:
    #     return 4
    # return 6

