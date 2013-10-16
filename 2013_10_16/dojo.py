#-*- coding: utf-8 -*-

import unittest

magic_square_3x3 = """
7 6 2
5 1 9
3 8 4
"""

def convert_str_to_square(text):
    square = []
    for line in text.strip().split("\n"):
        square.append([int(item) for item in line.strip().split()])

    return square


class Square(object):

    def __init__(self, input_square):
        if isinstance(input_square, basestring):
            self._square = convert_str_to_square(input_square)
        else:
            # TODO validate here
            self._square = input_square
        self.side = len(self._square)

    def rows(self):
        for row in self._square:
            yield row

    def columns(self):
        cols = []
        for col_index in range(self.side):
            col = []
            for row in self._square:
                col.append(row[col_index])
            cols.append(col)
        return cols

    def diagonals(self):
        diags = []

        for index




def validate(square):
    MAGIC_SUM = 15
    results = []

    for row in square.rows():
        results.append(sum(row))

    for column in square.columns():
        results.append(sum(column))

    return all([i == MAGIC_SUM for i in results])


def build(side):
    pass


class DojoTestCase(unittest.TestCase):

    def test_convert_str_to_square_3x3(self):
        example = """
        1 2 3
        4 5 6
        7 8 9
        """
        self.assertEqual(convert_str_to_square(example), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_convert_str_to_square_2x2(self):
        example = """
        1 2
        3 4
        """
        self.assertEqual(convert_str_to_square(example), [[1, 2], [3, 4]])

    def test_validate_invalid_3x3(self):
        square = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertFalse(validate(square))



if __name__ == "__main__":
    unittest.main()
