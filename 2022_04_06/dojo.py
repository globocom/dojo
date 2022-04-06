def main():
    return True


def parse_input(s: str):
    substrings = s.split(", ")
    return [(s[0], int(s[1:])) for s in substrings]


def walk(current, move):
    x, y, facing = current
    direction, steps = move
    facing_after_walk = determine_facing(facing, direction)
    if facing_after_walk == "N":
        return (x, y + steps, facing_after_walk)
    if facing_after_walk == "E":
        return (x + steps, y, facing_after_walk)
    if facing_after_walk == "S":
        return (x, y - steps, facing_after_walk)
    if facing_after_walk == "W":
        return (x - steps, y, facing_after_walk)
    else:
        raise RuntimeError("oops")


#     N
#  W     E
#     S


def determine_facing(facing, direction):
    all_facings = ["N", "E", "S", "W"]
    i = all_facings.index(facing)
    if direction == "R":
        return all_facings[(i + 1) % 4]
    return all_facings[(i - 1) % 4]


def manh_dist(x, y, d):
    return abs(x) + abs(y)


def aoc_1(input):
    moves = parse_input(input)
    position = (0, 0, "N")
    for move in moves:
        position = walk(position, move)
    return manh_dist(*position)


def aoc_2(input):
    moves = parse_input(input)
    seen = set(["0,0"])

    position = (0, 0, "N")
    for move in moves:
        position = walk(position, move)
        if f"{position[0]},{position[1]}" in seen:
            return manh_dist(*position)
        seen.add(f"{position[0]},{position[1]}")
        print(position, seen)
    return manh_dist(*position)


# 1. parse_input(str) -> [(dir, steps), ...]
# 2. walk(current=(x,y,dir), (dir, steps)) -> (x,y,dir)
# 3. descobrir o ponto final
# 4. distance(x,y,dir) -> int  # distancia final: x + y


# . . . . . . .
# . . 7 6 5 . .
# . . . . 4 . .
# . . . . 3 . .
# . . X 1 2 . .
# . . . . . . .
# . . . . . . .


# Bruno
# Henrique
# Tiago
