import hashlib

def main(secret, n=5):
    i = 1
    while not validate(secret, i, n):
        i += 1

    return i

def validate(secret, key, n=5):
    myhash = hashlib.md5(f"{secret}{key}".encode('utf-8')).hexdigest()
    return myhash[:n] == "0"*n



# Pedro
# Tiago
# Raphael
# Christian
# Giulio
# Bruno

# - Receber a secret_key como input
# - Dentro de um laço gerar um numero começando por 1
#   - Criar metodo que recebe a secret_key e o numero a ser testado
#   - Concatenar a secret_key com o numero
#   - Gerar o hash md5
#   - Validar se o hash começa com com 00000
#.  - Retornar se for valido.

