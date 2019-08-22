from itertools import cycle


class Robot():
    def __init__(self, position):
        self.position = position

    def turn_right(self):
        positions = ["T", "R", "D", "L", "T"]
        return positions[positions.index(self.position) + 1]

    def turn_left(self):
        positions = ["T", "L", "D", "R", "T"]
        return positions[positions.index(self.position) + 1]
