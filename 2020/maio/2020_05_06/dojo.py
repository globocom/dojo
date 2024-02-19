import math


def remove_white_spaces(sentence):
    return sentence.replace(' ', '')


def get_square_root_of_length(sentence):
    sqrt_root = math.sqrt(len(sentence))
    sqrt_ceil = math.ceil(sqrt_root)
    sqrt_floor = math.floor(sqrt_root)

    return [sqrt_floor, sqrt_ceil]


def get_matrix(sentence, sizes):
    x = 0
    array = []
    for x in range(sizes[0]):
        array.append(sentence[x: x+sizes[1]])

    return array
    # sentence[x : x+sizes[1]]
    # if sentence == "aaabbbcccbbb":
    # 	return [['aaab'], ['bbcc'], ['cbbb']]
    # if sentence == "haveawonderfulday":
    # 	return [['havea'], ['wonde'], ['rfuld'], ['ay']]
    # return [['havewo'], ['nderfu'], ['lniceg'], ['oodoka'], ['yday']]
