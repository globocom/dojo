def opposite_directions(first_dir, second_dir):
    cases = {
        "NORTH": "SOUTH", 
        "WEST": "EAST", 
        "SOUTH": "NORTH", 
        "EAST": "WEST"
    }
    return cases[first_dir] == second_dir

def main(input_list):
    stack = [] 
    for case in input_list:
        if len(stack) and opposite_directions(stack[-1], case):
            stack.pop()
        else:
            stack.append(case)
    return stack
