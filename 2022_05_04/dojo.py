from hashlib import md5

def main():
    return True

def compute_hash(input):
    hash = md5(input.encode('utf8')).hexdigest()
    return hash

def process(input):
    result = ''
    i=0
    while len(result) < 8:
        i+=1
        hash = compute_hash(f"{input}{i}")
        if (hash.startswith("00000")):
            result += hash[5]

    return result

def process_2(input):
    result = [' '] * 8
    i=0
    while ' ' in result:
        i+=1
        hash = compute_hash(f"{input}{i}")
        index = int(hash[5], base=16)
        if hash[:5] == "00000" and index < 8:
            if result[index] != ' ':
                continue
            result[index] = hash[6]

    return ''.join(result)
    # return "05ace8e3"



# Raphael
# Rafael 
# Christian
# Pedro 
# 
# 18f47a30
# oi oi, tudo bem?  - tcarreira


# Door ID ffykfhsq
# 
# 2 - dentro de um loop (process)
# 2.1 - concatenar Door ID com um sequencial iniciado por 0
# 2.2 - calcular o md5 hash do doorId + seq (compute_validate_hash)
# 2.3 - verificar se o calculo começa com '00000'
# 2.4 - caso positivo, guardar o caracter na posição 5
# 2.5 - seguir o loop ate ter 8 caracteres na senha
# 

