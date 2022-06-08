def main():
    return True

def get_square_cordinate(value):
    x_max = 0
    y_max = 0
    x_min = 0
    y_min = 0
    direction = (1,0)
    coord = (0,0)
    for i in range(value - 1):
        if coord[0] > x_max:
            x_max += 1
            direction = (0,1)
        if coord[1] > y_max:
            y_max += 1
            direction = (-1, 0)
        if coord[0] < x_min:
            x_min -= 1
            direction = (0, -1)
        if coord[1] < y_min:
            y_min -= 1
            direction = (1, 0)

        coord = (coord[0] + direction[0] , coord[1] + direction[1])
    
    return coord

def day_part_one(value):
    coord = get_square_cordinate(value)
    return abs(coord[0]) + abs(coord[1])



# -=== Ordem ====-
# Raphael
# Tiago
# Christian
# PEdro
# Luciana
# Matheus

# Baby steps
# 1 - getSquareCordinate
# 1.1 - recebe um valor e retorna a cordenada x,y desse valor
# 1.2 - 
