def main():
    
    return True

def aoc_1(input):
    answer = ""
    last_digit = 5
    for line in input.split("\n"):
        last_digit = process_line(line, last_digit)
        answer = f"{answer}{last_digit}"

    return int(answer)

def aoc_2(input):
    answer = ""
    last_digit = 5
    for line in input.split("\n"):
        last_digit = process_line_2(line, last_digit)
        answer = f"{answer}{last_digit}"

    return answer

def process_line(line, start_step):
    last_step = start_step
    for c in line:
        last_step = process_command(c, last_step)
    
    return last_step

def process_line_2(line, start_step):
    last_step = start_step
    for c in line:
        last_step = process_command_2(c, last_step)
    
    return last_step

def process_command(char, last_step):
    if char == "L":
        return {
            1: 1,
            2: 1,
            3: 2,
            4: 4,
            5: 4,
            6: 5,
            7: 7,
            8: 7,
            9: 8,
        }[last_step]
    if char == "U":
        return {
            1: 1,
            2: 2,
            3: 3,
            4: 1,
            5: 2,
            6: 3,
            7: 4,
            8: 5,
            9: 6,
        }[last_step]
    if char == "R":
        return {
            1: 2,
            2: 3,
            3: 3,
            4: 5,
            5: 6,
            6: 6,
            7: 8,
            8: 9,
            9: 9,
        }[last_step]
    if char == "D":
        return {
            1: 4,
            2: 5,
            3: 6,
            4: 7,
            5: 8,
            6: 9,
            7: 7,
            8: 8,
            9: 9,
        }[last_step]

    raise RuntimeError("Character unreachable")


def process_command_2(char, last_step):
    if char == "L":
        return {
            1: 1,
            2: 3,
            3: 2,
            4: 3,
            5: 5,
            6: 5,
            7: 6,
            8: 7,
            9: 8,
            'A': 'A',
            'B': 'A',
            'C': 'B',
            'D': 'D'
        }[last_step]
    if char == "U":
        return {
            1: 1,
            2: 2,
            3: 1,
            4: 4,
            5: 5,
            6: 2,
            7: 3,
            8: 4,
            9: 9,
            'A': 6,
            'B': 7,
            'C': 8,
            'D': 'B'
        }[last_step]
    if char == "R":
        return {
            1: 1,
            2: 3,
            3: 4,
            4: 4,
            5: 6,
            6: 7,
            7: 8,
            8: 9,
            9: 9,
            'A': 'B',
            'B': 'C',
            'C': 'C',
            'D': 'D'
        }[last_step]
    if char == "D":
        return {
            1: 3,
            2: 6,
            3: 7,
            4: 8,
            5: 5,
            6: 'A',
            7: 'B',
            8: 'C',
            9: 9,
            'A': 'A',
            'B': 'D',
            'C': 'C',
            'D': 'D'
        }[last_step]

    raise RuntimeError("Character unreachable")
