

# 1 - ler a linha lendo cada caracter
# 1.1 - se for um caracter nao ponto:
# 1.1.1 - ler a linha anterior com o i - 1, i e i + 1
# 1.1.2 - ler a linha proxima com o i - 1, i e i + 1
# 1.1.3 - se tiver um numero entre esses index lidos:
# 1.1.4 - completar o numero lendo da esquerda ou da direta até acabar numero
# 1.1.5 - salvar o numero com o linha,index
# 1.1.6 - adicionar o numero na variavel aux se não existir no mapa
# 2 - retorna variavel aux

def main():
    return True


# 4361
def read_lines(lines):
    count = 0
    for index, line in enumerate(lines):
        for ci, c in enumerate(line):
            if c != "." and not c.isnumeric():
                upper_num1 = return_number_in_line(lines[index -1], ci - 1)
                upper_num2 = return_number_in_line(lines[index -1], ci)
                upper_num3 = return_number_in_line(lines[index -1], ci + 1)
                
                if upper_num1 == upper_num2 and upper_num1 == upper_num3:
                    count += upper_num1
                elif upper_num1 > 0 and upper_num1 == upper_num2:
                    count += upper_num2
                elif upper_num2 > 0 and upper_num2 == upper_num3:
                    count += upper_num3
                else:
                    count += (upper_num1 + upper_num2 + upper_num3)

                count += return_number_in_line(lines[index], ci - 1)
                count += return_number_in_line(lines[index], ci + 1)

                lower_num1 = return_number_in_line(lines[index +1], ci - 1)
                lower_num2 = return_number_in_line(lines[index +1], ci)
                lower_num3 = return_number_in_line(lines[index +1], ci + 1)

                if lower_num1 == lower_num2 and lower_num1 == lower_num3:
                    count += lower_num1
                elif lower_num1 > 0 and lower_num1 == lower_num2:
                    count += lower_num2
                elif lower_num2 > 0 and lower_num2 == lower_num3:
                    count += lower_num3
                else:
                    count += (lower_num1 + lower_num2 + lower_num3)
                

    return count

def read_lines_gear(lines):
    count = 0
    for index, line in enumerate(lines):
        for ci, c in enumerate(line):
            if c == "*":
                upper_num1 = return_number_in_line(lines[index -1], ci - 1)
                upper_num2 = return_number_in_line(lines[index -1], ci)
                upper_num3 = return_number_in_line(lines[index -1], ci + 1)
                
                if upper_num1 == 0 and upper_num2 == 0 and upper_num3 == 0:
                    count += 0
                elif upper_num1 > 0 and upper_num2 > 0:
                    count += (upper_num1 * upper_num2)
                elif upper_num1 > 0 and upper_num3 > 0:
                    count += (upper_num1 * upper_num3)
                elif upper_num2 > 0 and upper_num3 > 0:
                    count += (upper_num2 * upper_num3)

                middle1 = return_number_in_line(lines[index], ci - 1)
                middle2 = return_number_in_line(lines[index], ci + 1)

                if middle1 > 0 and middle2 > 0:
                    count += (middle1 * middle2)

                lower_num1 = return_number_in_line(lines[index +1], ci - 1)
                lower_num2 = return_number_in_line(lines[index +1], ci)
                lower_num3 = return_number_in_line(lines[index +1], ci + 1)

                if lower_num1 == 0 and lower_num2 == 0 and lower_num3 == 0:
                    count += 0
                elif lower_num1 > 0 and lower_num2 > 0:
                    count += (lower_num1 * lower_num2)
                elif lower_num1 > 0 and lower_num3 > 0:
                    count += (lower_num1 * lower_num3)
                elif lower_num2 > 0 and lower_num3 > 0:
                    count += (lower_num2 * lower_num3)
                

    return count
#467..114..
#2

def return_number_in_line(line, index):
    if index < 0 or index == len(line) or not line[index].isnumeric():
        return 0
    
    left = return_number_in_line_left(line, index - 1) or ""
    right = return_number_in_line_right(line, index) or ""
    
    return int((left + right) or "0")

def return_number_in_line_left(line, index):
    if index < 0 or index == len(line) or not line[index].isnumeric():
        return None
    
    num = line[index]
    ant_num = return_number_in_line_left(line, index - 1)
    if ant_num is None:
        ant_num = num
    else:
        ant_num += num
    
    return ant_num

def return_number_in_line_right(line, index):
    if index < 0 or index == len(line) or not line[index].isnumeric():
        return None
    
    num = line[index]
    ant_num = return_number_in_line_right(line, index + 1)
    if ant_num is not None:
        num += ant_num
    
    return num
