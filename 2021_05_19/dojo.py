def function_right(password, guess):
    return sum(password[i] == guess[i] for i, _ in enumerate(password))
    

def function_in(password, guess):
    return len(set(password) & set(guess))


def main(password, guess):
    right = function_right(password, guess)
    fin = function_in(password, guess)
    return f"{right}-{fin - right}"

