def decode_way(code):
    combination = 1

    for i, digit in enumerate(code):
        if i+1 >= len(code):
            break

        combination += greater(digit+code[i+1])

    return combination


def greater(digit):
    if int(digit) > 26:
        return 0
    return 1
