import math

def get_dimensions(sentence):
    square_root = math.sqrt(len(sentence))
    lines = math.floor(square_root)
    columns = math.ceil(square_root)

    if columns * lines < len(sentence):
        return (columns, columns)
    
    return (lines, columns)


def build_matrix(sentence):
    sentence_without_spaces = sentence.replace(" ", "")
    lines, columns  = get_dimensions(sentence_without_spaces)

    matrix = [[""]*columns for _ in range(lines)]

    for i in range(lines):
        for j in range(columns):
            index = columns*i + j   
            if index >= len(sentence_without_spaces):
                break
            matrix[i][j] = sentence_without_spaces[ index ]
    return matrix


