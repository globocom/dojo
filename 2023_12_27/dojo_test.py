import unittest
from dojo import *

input = """Game 1: 4 red, 5 blue, 9 green; 7 green, 7 blue, 3 red; 16 red, 7 blue, 3 green; 11 green, 11 blue, 6 red; 12 red, 14 blue
Game 2: 12 blue, 11 green, 3 red; 6 blue, 5 green, 7 red; 5 red, 11 blue; 2 blue, 8 green
Game 3: 8 blue, 5 green, 2 red; 5 blue, 5 green, 7 red; 7 blue, 1 green, 7 red; 8 green, 14 blue, 7 red; 8 green, 14 blue; 8 blue, 2 green, 8 red
Game 4: 3 red, 14 blue, 15 green; 1 red, 11 green, 14 blue; 14 green, 17 blue
Game 5: 11 green, 2 red, 10 blue; 16 green, 8 blue; 2 blue, 6 green, 1 red; 14 blue, 2 red, 16 green; 3 blue, 18 green; 1 red, 10 blue, 3 green
Game 6: 2 green, 5 red, 17 blue; 12 green, 13 blue, 6 red; 8 red, 9 blue, 7 green
Game 7: 2 blue, 18 green; 4 green, 1 red, 1 blue; 4 blue, 19 green
Game 8: 6 green, 7 blue; 9 green, 6 blue; 7 blue, 1 red, 3 green
Game 9: 4 blue, 12 green, 3 red; 4 green, 3 blue, 3 red; 3 green, 2 red, 3 blue; 1 green, 2 red, 3 blue; 15 red, 10 green, 4 blue; 3 blue, 1 red, 6 green
Game 10: 11 blue, 6 green, 6 red; 15 green, 1 blue; 1 red, 6 blue, 4 green
Game 11: 9 blue, 1 red, 6 green; 6 red, 1 green; 10 blue, 3 green, 6 red
Game 12: 1 blue, 10 red, 1 green; 4 blue, 4 red; 8 red, 3 blue, 1 green; 3 red, 2 green
Game 13: 3 red, 11 green, 18 blue; 11 green, 1 red, 3 blue; 12 blue, 5 red, 2 green; 16 blue, 8 red, 5 green; 8 red, 12 blue, 19 green; 17 blue, 4 green, 6 red
Game 14: 8 red, 4 blue; 1 green, 2 blue, 13 red; 1 green, 1 blue, 17 red; 1 green, 13 red
Game 15: 4 red, 3 blue, 6 green; 4 blue, 3 red, 3 green; 3 green, 6 red, 3 blue; 6 red, 5 blue, 2 green; 6 green, 1 blue; 4 green, 3 red, 2 blue
Game 16: 11 green; 3 green, 1 blue, 1 red; 12 green, 3 blue, 1 red; 1 red, 1 green; 1 red, 3 blue; 2 green, 1 blue, 1 red
Game 17: 12 red, 14 blue, 10 green; 2 red, 6 green, 6 blue; 10 blue, 2 green, 3 red; 1 red, 13 blue, 2 green; 9 green, 16 red, 9 blue
Game 18: 15 red, 8 blue; 16 red, 12 blue; 5 blue, 4 green, 6 red; 8 red, 4 green, 3 blue; 7 red, 5 blue, 2 green; 1 blue, 2 green, 14 red
Game 19: 3 red, 13 blue, 2 green; 8 red, 14 blue; 9 blue, 3 green; 9 blue, 1 green, 7 red; 8 red, 1 green; 8 red, 14 blue, 2 green
Game 20: 6 green, 10 blue, 5 red; 8 green, 9 blue, 7 red; 2 red, 2 green, 7 blue; 7 red, 16 green, 12 blue; 15 green, 3 red; 12 green, 3 red, 6 blue
Game 21: 2 green, 7 blue; 7 blue, 6 red; 6 blue, 2 red, 1 green; 11 blue, 1 red, 3 green
Game 22: 5 red, 1 blue; 1 green, 2 red; 1 blue, 1 green, 5 red; 1 green, 2 blue, 4 red; 1 green, 3 red, 1 blue; 5 red, 3 blue, 1 green
Game 23: 12 green, 7 red; 4 blue, 15 red, 2 green; 2 green, 16 red, 2 blue; 5 red, 10 green, 1 blue; 1 red, 4 green, 7 blue; 9 blue, 4 green, 12 red
Game 24: 7 blue, 11 red, 4 green; 6 blue, 3 green; 1 blue, 14 red, 1 green; 2 blue, 4 green, 15 red; 7 red, 4 blue; 7 red, 2 blue, 3 green
Game 25: 6 green, 10 red, 12 blue; 3 red, 16 blue; 10 blue, 10 red, 1 green; 3 red, 2 green, 13 blue; 2 green, 11 blue, 6 red
Game 26: 6 red, 4 blue, 10 green; 3 blue, 1 green, 4 red; 5 blue; 11 blue, 9 green, 7 red
Game 27: 1 red, 14 green, 9 blue; 13 green, 8 blue, 8 red; 7 red, 8 green, 6 blue; 7 blue, 3 red, 4 green; 18 green, 3 red
Game 28: 2 red, 1 blue, 1 green; 1 blue; 1 red, 6 green, 2 blue; 5 green, 1 blue; 6 green; 2 green, 5 blue, 2 red
Game 29: 2 blue, 2 green, 7 red; 3 red, 5 blue; 7 green, 14 blue, 3 red
Game 30: 5 red, 11 green, 8 blue; 1 blue, 1 red, 15 green; 18 green, 12 blue; 5 red, 6 blue, 16 green; 12 blue, 1 red, 5 green
Game 31: 1 blue, 7 red, 2 green; 8 green, 1 blue; 3 blue, 13 green, 2 red; 3 blue, 7 red
Game 32: 10 green, 7 blue, 4 red; 18 green, 4 blue, 7 red; 5 blue, 6 red; 5 red, 5 blue, 1 green; 12 blue, 5 green, 8 red; 1 red, 6 green, 13 blue
Game 33: 1 green, 2 red, 18 blue; 12 blue, 8 green; 8 green, 1 red, 16 blue; 10 green, 14 blue; 1 red, 3 blue, 8 green
Game 34: 4 red, 4 blue; 10 blue, 8 red; 2 green, 5 blue, 20 red
Game 35: 6 blue, 1 green, 4 red; 1 red, 2 blue, 2 green; 12 blue, 2 red; 11 blue, 1 green, 1 red; 2 blue; 2 red, 10 blue, 3 green
Game 36: 2 green, 9 blue, 11 red; 5 blue, 11 red; 1 green, 1 red, 9 blue; 8 blue, 2 green; 11 red, 4 blue, 1 green; 7 blue, 2 green, 5 red
Game 37: 10 blue, 5 green, 6 red; 5 red, 13 green, 10 blue; 1 green, 7 blue, 4 red; 10 green, 4 blue, 14 red; 13 green, 9 red, 1 blue
Game 38: 5 blue, 4 green, 4 red; 4 blue, 11 green; 4 green, 3 red; 6 green, 7 blue; 6 blue, 1 red, 2 green
Game 39: 8 blue, 1 green, 19 red; 15 red, 2 green, 7 blue; 1 green, 6 blue, 8 red; 16 red, 3 blue, 1 green
Game 40: 4 green, 1 blue; 1 red, 2 blue, 3 green; 4 green, 1 blue, 2 red; 2 green, 1 blue, 2 red; 2 green
Game 41: 3 red, 4 blue; 2 blue, 16 green; 2 red, 5 blue, 11 green; 13 green, 3 red, 6 blue; 3 blue, 19 green, 3 red; 5 green, 1 red, 3 blue
Game 42: 6 green; 13 green, 1 blue; 1 blue, 5 green, 1 red; 1 blue, 6 green, 1 red; 2 red, 2 green, 1 blue
Game 43: 8 green, 11 blue; 11 green, 12 blue; 1 blue, 5 red, 7 green; 1 blue, 11 green; 3 blue, 1 green
Game 44: 3 green, 18 red, 16 blue; 2 blue, 2 green, 14 red; 13 red, 4 green, 17 blue; 3 red, 9 blue, 8 green; 11 red, 1 blue; 5 blue, 3 red, 7 green
Game 45: 11 blue, 2 red; 8 green, 5 blue, 1 red; 14 blue, 5 green; 14 blue, 8 green; 10 blue, 11 green; 5 green, 1 red, 17 blue
Game 46: 3 red, 3 blue, 1 green; 2 green, 7 red, 4 blue; 2 red, 1 green, 2 blue; 9 red, 1 green
Game 47: 3 blue, 4 red, 2 green; 9 blue, 12 green, 11 red; 8 green, 19 red, 7 blue
Game 48: 1 green, 9 red; 7 green, 16 red, 1 blue; 2 blue, 2 red, 5 green; 19 red, 3 blue, 2 green
Game 49: 2 green, 17 blue, 18 red; 4 blue, 19 red, 11 green; 1 green, 5 blue, 15 red; 10 green, 6 red, 1 blue
Game 50: 4 green, 8 blue, 6 red; 1 red, 6 blue, 4 green; 6 red, 5 green, 10 blue; 7 blue, 6 red
Game 51: 2 green, 1 blue, 5 red; 13 blue, 10 green; 6 green, 1 red, 7 blue; 4 red, 3 green, 8 blue; 3 red, 9 blue, 4 green; 2 red, 12 blue, 8 green
Game 52: 1 blue, 4 green, 6 red; 6 green, 6 red, 10 blue; 4 green, 3 red, 5 blue; 3 blue, 2 green, 4 red; 6 green, 5 blue, 9 red; 9 red, 5 green, 8 blue
Game 53: 2 green, 6 blue, 6 red; 1 blue, 5 green, 13 red; 7 red, 5 blue, 1 green
Game 54: 5 green, 6 blue, 2 red; 1 blue, 3 green; 6 green; 1 red, 2 blue, 5 green; 5 blue, 5 green
Game 55: 9 blue, 15 green; 4 red, 1 green; 7 blue, 9 red, 11 green
Game 56: 7 red, 2 blue, 4 green; 2 blue, 6 red, 6 green; 8 red, 7 green; 6 green, 2 red; 3 blue, 2 green, 7 red
Game 57: 1 blue, 1 green, 1 red; 6 red, 2 green, 3 blue; 1 green; 3 blue, 8 red, 2 green
Game 58: 14 blue, 5 red, 14 green; 5 blue, 7 green, 7 red; 19 blue, 10 red, 14 green; 7 green, 5 blue, 10 red; 2 red, 12 green, 2 blue
Game 59: 1 red, 1 green, 1 blue; 10 blue; 3 blue, 1 green, 1 red
Game 60: 6 blue, 6 green; 5 blue; 4 blue, 3 green; 10 green, 1 red, 4 blue
Game 61: 2 green, 3 blue; 3 red, 3 blue; 2 red, 4 green
Game 62: 3 red, 6 green, 2 blue; 6 red, 5 blue, 2 green; 13 green, 9 blue
Game 63: 9 blue, 1 green; 14 blue, 12 red; 1 green, 6 red, 14 blue; 1 green, 2 red, 14 blue; 7 red, 18 blue, 1 green; 14 red, 2 blue
Game 64: 4 blue, 16 red, 4 green; 9 red, 4 green, 3 blue; 2 red, 2 blue, 6 green; 2 blue, 2 green, 12 red
Game 65: 2 red, 2 blue; 4 red, 9 green, 5 blue; 1 blue; 3 green, 1 red; 1 green, 2 blue, 8 red; 1 blue, 8 green, 3 red
Game 66: 1 red, 3 green, 4 blue; 3 green, 5 red, 14 blue; 1 blue, 3 red, 2 green; 4 blue, 1 green, 2 red; 8 red, 2 green, 13 blue
Game 67: 1 green, 1 red, 4 blue; 2 blue, 2 green, 1 red; 3 blue, 2 green, 1 red
Game 68: 1 red, 2 blue; 5 green, 2 red, 2 blue; 7 red, 7 green, 2 blue
Game 69: 15 red, 12 green, 1 blue; 3 green, 3 blue, 6 red; 9 blue, 16 green; 11 blue, 18 green, 7 red
Game 70: 4 blue, 1 green, 6 red; 11 red, 3 green, 4 blue; 3 blue, 1 red, 1 green; 1 green, 11 red; 3 red, 4 blue, 1 green; 3 red, 4 blue, 2 green
Game 71: 11 blue, 1 red; 10 blue, 10 green; 4 green, 11 blue; 5 green, 1 red, 6 blue; 6 green, 2 blue; 4 blue, 3 green
Game 72: 1 red, 7 blue; 3 red, 3 green, 7 blue; 3 red, 3 green, 10 blue; 5 green, 7 blue
Game 73: 2 blue, 1 red; 6 blue, 8 red, 18 green; 4 blue, 18 green, 1 red; 1 red, 5 blue, 2 green; 18 green, 8 red, 8 blue
Game 74: 19 green, 9 blue, 14 red; 11 green, 8 blue, 14 red; 2 green, 17 blue, 14 red; 12 green, 12 blue, 7 red; 6 red, 5 blue, 10 green; 4 blue, 19 green, 15 red
Game 75: 12 red, 3 green, 4 blue; 7 red, 6 green, 2 blue; 7 green, 3 red, 7 blue; 16 red, 3 green; 10 blue, 6 red, 3 green
Game 76: 1 red, 11 blue, 4 green; 11 green, 3 blue, 3 red; 2 red, 14 green, 7 blue; 3 red, 6 blue, 9 green; 9 blue, 14 green; 1 red, 9 green, 3 blue
Game 77: 10 blue, 2 red, 5 green; 5 green, 3 red, 12 blue; 3 green, 8 red, 4 blue; 5 blue, 12 red, 7 green; 18 blue, 7 red; 8 green, 8 blue, 13 red
Game 78: 9 red, 11 green, 4 blue; 4 blue, 14 green; 2 red, 11 green, 6 blue; 2 blue, 5 red, 13 green; 6 red, 2 green
Game 79: 2 green, 3 blue, 1 red; 6 green, 2 blue; 1 blue, 4 green
Game 80: 2 green, 4 red; 1 green, 6 blue, 2 red; 8 blue, 3 red; 6 blue, 1 green; 6 red, 2 blue; 2 green, 2 blue
Game 81: 5 red, 3 blue, 6 green; 3 blue, 17 green, 5 red; 3 red, 2 blue, 14 green; 1 blue, 2 red, 8 green
Game 82: 16 green, 10 blue; 6 blue, 4 green, 2 red; 3 blue, 1 red, 16 green; 1 red, 7 green, 11 blue
Game 83: 8 green, 7 blue; 1 blue, 6 green; 6 blue, 1 red, 3 green; 8 green, 1 red; 1 green, 5 blue
Game 84: 9 blue, 6 red; 5 red, 7 green, 3 blue; 4 blue, 13 green, 2 red; 10 red, 11 green, 6 blue
Game 85: 4 red, 10 blue; 8 green, 1 blue, 1 red; 9 blue, 6 green; 1 red, 4 green; 3 green, 8 blue
Game 86: 7 blue, 9 green; 7 blue, 1 red, 4 green; 4 green, 13 blue
Game 87: 12 red, 9 green, 2 blue; 8 green, 7 red; 11 red, 11 green; 4 blue, 8 green
Game 88: 8 blue, 7 green, 7 red; 5 blue, 9 green; 3 red, 7 green, 6 blue; 1 green, 7 blue, 7 red
Game 89: 7 green, 9 red, 7 blue; 1 green, 18 red; 3 red, 2 blue, 2 green; 15 red, 4 green, 6 blue
Game 90: 4 blue, 5 red, 4 green; 4 green, 6 blue, 3 red; 4 green, 6 blue, 2 red; 8 blue, 4 red, 4 green; 3 blue, 2 red
Game 91: 7 green, 5 red, 2 blue; 12 green, 2 blue, 6 red; 6 green, 1 blue; 1 green, 1 blue; 13 green, 1 red, 3 blue; 5 red, 1 blue, 4 green
Game 92: 2 green; 1 red, 2 blue, 2 green; 2 red, 2 green, 2 blue; 2 blue, 7 red
Game 93: 8 red, 5 blue; 10 red, 4 blue; 3 red, 2 blue; 7 blue, 10 red, 1 green; 6 blue; 10 blue
Game 94: 2 blue, 4 green; 8 green, 9 blue; 2 green, 3 blue; 3 blue, 5 green; 9 blue, 1 red, 3 green; 6 blue, 6 green, 1 red
Game 95: 3 blue, 13 red, 10 green; 4 green, 17 blue, 12 red; 12 red, 10 green, 16 blue; 15 red, 14 green, 2 blue; 12 red, 1 blue, 15 green; 10 green, 13 blue, 19 red
Game 96: 5 green, 9 blue, 16 red; 17 red, 11 green, 9 blue; 10 blue, 13 green, 9 red; 10 blue, 7 red, 13 green; 3 red, 4 blue, 5 green
Game 97: 6 blue, 4 green, 6 red; 4 red, 13 green, 2 blue; 15 green, 2 red; 2 green, 2 red
Game 98: 10 blue, 13 red; 10 blue, 16 red, 4 green; 6 blue, 4 green, 14 red; 4 green, 1 blue, 11 red; 4 red, 4 green
Game 99: 1 red, 4 blue; 5 red, 8 blue; 3 blue, 1 green; 2 red, 6 blue; 8 blue, 2 green, 3 red
Game 100: 5 green, 1 red; 4 blue, 8 red, 4 green; 1 blue, 3 red, 15 green; 1 blue, 15 green, 1 red; 2 red, 13 green""".strip().split("\n")

example_1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".strip().split("\n")

class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(main())

    def test_day_2_1(self):
        self.assertEqual(day_2_1(input), 2795)
    
    def test_day_2_1_example(self):
        self.assertEqual(day_2_1(example_1), 8)

    def test_day_2_1(self):
        self.assertEqual(day_2_2(input), 75561)
    
    def test_day_2_1_example(self):
        self.assertEqual(day_2_2(example_1), 2286)

if __name__ == '__main__':
    unittest.main()
