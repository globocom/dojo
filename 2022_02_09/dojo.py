def main(presents):
    total = 0
    for line in presents.splitlines():
        total += get_present_area(parse_present(line))

    return total


def parse_present(present_str):
    # return list(map(int, present_str.split("x")))
    return [int(l) for l in present_str.split("x")]


def calculate_areas(present):
    l, w, h = present
    return [l * w, w * h, h * l]


def get_min_area(areas):
    return min(areas)


def get_present_area(present):
    areas = calculate_areas(present)
    extra = get_min_area(areas)

    return 2 * areas[0] + 2 * areas[1] + 2 * areas[2] + extra


# (length l, width w, and height h)
# Input format :(l*w*h)
# Areas formula: 2*l*w + 2*w*h + 2*h*l

# 0. por cada linha:
#   1. Ler o input: parse_present("2x3x4") -> [2, 3, 4]
#   2. Somar area por presente: get_present_area([2, 3, 4]) -> 58
#      2.1 Calcular área de cada lado: calculate_areas([2, 3, 4]) -> [6, 12, 8]
#      2.2 Pegar menor área: get_min_area([6, 12, 8]) -> 6
#      2.3 Return 2x6 + 2x12 + 2x8 + 6
# 0.1. somar a área de todos os presentes usando get_present_area()

##########
# Tiago
# Pedro
# Raphael
# Paulo
# Juliana
# Christian
