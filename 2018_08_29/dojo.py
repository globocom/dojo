from itertools import cycle

def main(value):
    column = len(value)
    line1 = [None] * column
    line2 = [None] * column
    line3 = [None] * column
    matrix = [line1,line2,line3]

    j = 0
    for i in cycle([0, 1, 2, 1]):
        matrix[i][j] = value[j]
        j += 1
        if j >= column:
            break

    return matrix