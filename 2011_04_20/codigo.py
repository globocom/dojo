import string 

def palavra_eh_primo(palavra):
    valor_palavra = 0
    
    for letra in palavra:
        valor_palavra += string.letters.find(letra)+1
    
    return num_eh_primo(valor_palavra)
    
def num_eh_primo(num):
    if num <= 1:
        return False    
        
    for i in range(2,num):
        if num % i == 0:
            return False
    return True