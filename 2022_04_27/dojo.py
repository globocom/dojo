from collections import Counter

def main():
    return True

def split_string(line):
    split = line.split("-")
    room = "-".join(split[:-1])

    sector_and_checksum = split[-1].split("[")
    
    sector_id = int(sector_and_checksum[0])
    checksum = sector_and_checksum[1][:-1]

    return (room, sector_id, checksum)

def count_letter(room):
    room = "".join(room.split("-"))
    return Counter(room)

    # count_letter_dict = {}
    # for char in room:
    #     if char in count_letter_dict:
    #         count_letter_dict[char] += 1
    #     else:
    #         count_letter_dict[char] = 1
    # return count_letter_dict


def checksum_from_count(count):
    sorted_count = sorted(count.items(), key=lambda x: (-x[1],x[0]))

    sorted_keys = [x[0] for x in sorted_count]
    checksum = "".join(sorted_keys[:5])
    
    return checksum

def compute_checksum(room):
    return checksum_from_count(count_letter(room))

def aoc_day_one(input):
    solution = 0
    for line in input.split("\n"):
        room, sector, checksum = split_string(line)
        if checksum == compute_checksum(room):
            solution += sector
    return solution

def shift_name(room, sector):
    solution = ""
    rotations = sector % 26
    for char in room:
        if char == '-':
            solution += ' '
            continue
        
        ascii_char = ord(char) # a -> 97, z->122
        tmp_char = ascii_char + rotations
        if tmp_char > ord("z"):
            tmp_char -= 26
        
        solution += chr(tmp_char)

        
    return solution

def aoc_day_two(input):
    solution = 0
    for line in input.split("\n"):
        room, sector, checksum = split_string(line)
        if (shift_name(room, sector) == "northpole object storage"):
            solution = sector
            break
    
    return solution
# 
# process(input)
# 1 - separar a room, sector id e checksum
# 1.1 - split_string(line)
# 2 - Contar quantas vezes as letras aparecem na string do room
# 2.1 - compute_checksum(room) -> checksum
# 2.1.1 - count_letter(room) -> dict
# 2.1.2 - checksum_from_count(count_letter(room)) -> checksum
# 3 - checar se o checksum está batendo com as 5 primeiras letras apresentadas
# 3.1 - if checksum == checksum
# 4 - somar o sectorID se a room for valida
# 
