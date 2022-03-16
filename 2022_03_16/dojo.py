def contains_vowels(my_string):
    v_counter = 0
    for char in my_string:
        if char in ["a", "e", "i", "o", "u"]:
            v_counter += 1
            if v_counter >= 3:
                return True
    return False


def contains_double_letter(s):

    for pair in zip(s, s[1:]):
        if pair[0] == pair[1]:
            return True
    # for i in range(1, len(s)):
    #     if s[i] == s[i - 1]:
    #         return True

    return False


def contains_forbidden(s):
    if "ab" in s:
        return True
    if "cd" in s:
        return True
    if "pq" in s:
        return True
    if "xy" in s:
        return True
    return False


def validate_nice_string(s):
    return (
        contains_vowels(s) and contains_double_letter(s) and not contains_forbidden(s)
    )


def main():
    counter = 0
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            if validate_nice_string(line):
                counter += 1
    return counter


# 3 regras. Criar uma função para validar cada regra
#
# main():
#    iterar todas as strings do input:
#    validate_nice_string(s: string) -> bool
#       - contains_vowels() -> bool
#       - contains_double_letter() -> bool
#       - not_contains_forbidden() -> bool
#


# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.


# Dimas
# PAulo
# Chrirsitan
# Raphael Rossi
# Tiago
# Pedro
