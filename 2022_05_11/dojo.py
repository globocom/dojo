from collections import Counter

def main():
    return True

def line_to_column(line):
    return list(line.strip())

def column_to_string(list_of_lines):
    list_of_columns = [""]*len(list_of_lines[0])
    for line in list_of_lines:
        for c, char in enumerate(line):
            list_of_columns[c] = list_of_columns[c]+char
    
    return list_of_columns

def day_one(lines):
    list_of_lines = []
    for line in lines.split('\n'):
        list_of_lines.append(line_to_column(line))
    
    list_of_columns = column_to_string(list_of_lines)
    result = ""
    for column in list_of_columns:
        c = Counter(column)
        result += c.most_common(1)[0][0]

    return result

def day_two(lines):
    list_of_lines = []
    for line in lines.split('\n'):
        list_of_lines.append(line_to_column(line))
    
    list_of_columns = column_to_string(list_of_lines)
    result = ""
    for column in list_of_columns:
        c = Counter(column)
        result += c.most_common()[-1][0]

    return result
# 
# Raphael
# Rodolfo
# Pedro
# Christian
# Tiago
# 
# 1 - Contar a quantidade de caracters por linha
# 2 - Ler a linha em laço
# 2.1 - Transformar a linha em coluna
# 2.2 - Guardar a letra da coluna em um array
# 2.3 - Chamar a função de counter no array da coluna
# 3 - montar a palavra baseado nas letras mais repetidas

# list_of_words=['Cars', 'Cats', 'Flowers', 'Cats','Cats','Cats']
# from collections import Counter
# c = Counter(list_of_words)
# c.most_common(1)
# print ("",c.most_common(1))

# out:  [('Cats', 4)]
