def main():
    return True

def day_2_1(input):

    possible_ids = 0
    for line in input:
        games = line.split(":")

        id = int(games[0].split(" ")[1])
        sets = games[1].split(";")
        if is_set_valid(sets):
            possible_ids += id
    
    return possible_ids

def day_2_2(input):

    power_sum = 0
    for line in input:
        games = line.split(":")

        id = int(games[0].split(" ")[1])
        sets = games[1].split(";")
        power_sum += power_set_game(sets)
        
    return power_sum


def is_set_valid(sets):
    valid = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    
    for set in sets:
        cubes = set.split(", ")
        for cube in cubes:
            num = int(cube.strip().split(" ")[0])
            color = cube.strip().split(" ")[1]
            if num > valid[color]:
                return False

    return True


def power_set_game(sets):
    values = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for set in sets:
        cubes = set.split(", ")
        for cube in cubes:
            num = int(cube.strip().split(" ")[0])
            color = cube.strip().split(" ")[1]
            if num > values[color]:
                values[color] = num

    mult = 1
    for value in values:
        mult = values[value] * mult

    return mult
