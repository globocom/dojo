def main():
    return True

def to_lower(txt):
    return txt.lower()

def remove_pontuation(txt):
    output = ""
    for c in txt:
        if (
            ord("0") <= ord(c) <= ord("9")
        ) or (
            ord("a") <= ord(c) <= ord("z")
        ):
            output += c
    return output

def reverse_string(txt):
    return txt[::-1]

def is_palindrome(txt):
    formated_text = remove_pontuation(to_lower(txt))
    reversed_text = reverse_string(formated_text)

    return  formated_text == reversed_text
