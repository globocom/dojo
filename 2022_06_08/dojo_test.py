import unittest
from dojo import *


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(main())

    def test_cordinate_1(self):
        self.assertEqual(get_square_cordinate(1), (0,0))

    def test_cordinate_2(self):
        self.assertEqual(get_square_cordinate(2), (1,0))

    def test_cordinate_3(self):
        self.assertEqual(get_square_cordinate(3), (1,1))

    def test_cordinate_4(self):
        self.assertEqual(get_square_cordinate(4), (0,1))

    def test_cordinate_5(self):
        self.assertEqual(get_square_cordinate(5), (-1,1))
    
    def test_cordinate_6(self):
        self.assertEqual(get_square_cordinate(6), (-1,0))

    def test_cordinate_7(self):
        self.assertEqual(get_square_cordinate(7), (-1,-1))

    def test_cordinate_8(self):
        self.assertEqual(get_square_cordinate(8), (0,-1))

    def test_cordinate_9(self):
        self.assertEqual(get_square_cordinate(9), (1,-1))

    def test_cordinate_10(self):
        self.assertEqual(get_square_cordinate(10), (2,-1))

    def test_cordinate_23(self):
        self.assertEqual(get_square_cordinate(23), (0,-2))

    def test_day_part_one_2(self):
        self.assertEqual(day_part_one(1), 0 )
    def test_day_part_one_12(self):
        self.assertEqual(day_part_one(12), 3)
    def test_day_part_one_23(self):
        self.assertEqual(day_part_one(23), 2)
    def test_day_part_one_real_input(self):
        self.assertEqual(day_part_one(265149), 438)

# direction = (-1,0)
# x_max=1
# y_max=1
# 1 - (0,0)
# 2 - (1,0)
# 3 - (1,1)
# 4 - (0,1)

#    4 3
#    1 2



if __name__ == '__main__':
    unittest.main()


# 37  36  35  34  33  32  31 
# 38  17  16  15  14  13  30
# 39  18   5   4   3  12  29
# 40  19   6   1   2  11  28
# 41  20   7   8   9  10  27
# 42  21  22  23  24  25  26
# 43  44  45  46  47  48  49  50

