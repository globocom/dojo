def main(obj):
    return [1, 1]

def absolute_distance(tree, position):
    # if position == 5:
    #     return 20
    # return 9
    return tree + position

def parser_array_to_absolute(tree, position):    
    def iterable(i):
        return absolute_distance(tree, i)
    return map(iterable, position)

def is_inside(house, fruit):
    return fruit >= house[0] and fruit <= house[1]