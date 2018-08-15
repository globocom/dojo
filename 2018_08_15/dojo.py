class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def get_position(self):
        return self.x, self.y, self.direction

    def turn_right(self):
        return self.turn(['north', 'east', 'south', 'west', 'north'])

    def turn_left(self):
        return self.turn(['north', 'west', 'south', 'east', 'north'])


    def turn(self, position):
        i = position.index(self.direction)
        self.direction = position[i+1]

        return self.direction

    def advance(self):
        self.y += 1
        return (self.x, self.y, self.direction)