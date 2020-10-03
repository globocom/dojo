import unittest
from dojo import main
from dojo import absolute_distance
from dojo import parser_array_to_absolute
from dojo import is_inside


class DojoTest(unittest.TestCase):
    def test_case_1(self):
        obj = {
            "house": [7, 11],
            "apple_tree": 5,
            "orange_tree": 15,
            "apples": [-2, 2, 1],
            "oranges": [5, -6],
        }
        self.assertEqual(main(obj), [1, 1])

    def test_case_2(self):
        orange_tree = 15
        orange = 5
        self.assertEqual(absolute_distance(orange_tree, orange), 20)
        
    def test_case_3(self):
        orange_tree = 15
        orange = -6
        self.assertEqual(absolute_distance(orange_tree, orange), 9)

    def test_case_4(self):
        orange_tree = 15
        orange = 2
        self.assertEqual(absolute_distance(orange_tree, orange), 17)
    
    def test_case_5(self):
        fruits = [4, 10, 15]
        tree = 10
        self.assertEqual(parser_array_to_absolute(tree, fruits), [14, 20, 25])

    def test_case_6(self):
        fruits = [5, 10, 15]
        tree = 10
        self.assertEqual(parser_array_to_absolute(tree, fruits), [15, 20, 25])

    def test_case_7(self):
        house = [10, 15]
        fruit = 10
        self.assertEqual(is_inside(house, fruit), True)

if __name__ == '__main__':
    unittest.main()
