def main():
    return True


def split_string(text):
    text_list = text.split(" ")

    return_array = []
    for element in text_list:
        return_array.append(int(element)) 
    
    return return_array


def find_max(numbers):
    max_value = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
    
    return max_value
    
def find_min(numbers):
    min_value = numbers[0]
    for item in numbers:
        min_value = min(min_value, item)
    return min_value

def ans(min_value, max_value):
    return f"{max_value} {min_value}"

def high_and_low(text):
    array = split_string(text)
    max_value = find_max(array)
    min_value = find_min(array)
    
    result = ans(min_value, max_value)
    return result



def high_and_low_python_way(text):
    numbers = [ int(x) for x in text.split(" ") ]
    return f"{max(numbers)} {min(numbers)}"



# 1 - split dos números: string para em um array
# 2 - percorrer o array e guardar qual o maior e o menor
#   2.1 - funcao para encontrar o maior
#   2.2 - funcao para encontrar o menor
# 3 - retornar string com maior e menor



# TDD - Test Driven Development
# Baby Steps 

# Dojo 
# Piloto - Co-copiloto
# 3 minutos

# Primeiro escrevemos 1 teste
# escrevemos a função - apenas passar o teste
# Primeiro escrevemos 2 teste
# apenas passar o teste
# Primeiro escrevemos 3 teste
# apenas passar o teste
# Implementar lógica
