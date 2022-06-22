import unittest
from pathlib import Path
from dojo import *

# 5
example = '''
0
3
0
1
-3
'''.strip()


real_input = Path('input').read_text()



example_day_7 = '0 2 7 0'
input_day_7 = '0 5 10 0 11 14 13 4 11 8 8 7 1 4 12 11'


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_steps_part1(self):
        self.assertEqual(calculate_steps([0,3,0,1,-3]), 5)

    def test_real_input_part1(self):
        self.assertEqual(calculate_steps(list(map(int, real_input.strip().split("\n")))), 388611)

    def test_steps_part2(self):
        self.assertEqual(calculate_steps_part2([0,3,0,1,-3]), 10)

    def test_real_input_part2(self):
        self.assertEqual(calculate_steps_part2(list(map(int, real_input.strip().split("\n")))), 27763113)

    def test_get_max(self):
        self.assertEqual(get_max([1,4,3,4]),1)

    def test_get_max2(self):
        self.assertEqual(get_max([1,3,4,4]),2)

    def test_get_max3(self):
        self.assertEqual(get_max([4]),0)

    def test_val_count(self):
        self.assertEqual(get_count([0,2,7,0]), 5)

    def test_val_count_real_input(self):
        self.assertEqual(get_count(list(map(int, input_day_7.split(" ")))), 5)

if __name__ == '__main__':
    unittest.main()


# hello world - tcarreira

# Caio
# Matheus
# Raphael
# Ygor
# Pedro
# Carreira
# Ademario
# Ingrid

# ------ DAY 6

##### 
#    0 2 7 0
###  0 2 0 0  (7)
#    2 4 1 2


# 0 2 7 0 - 4
# 0 5 10 0 11 14 13 4 11 8 8 7 1 4 12 11 - 16
