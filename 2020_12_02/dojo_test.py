import unittest
from dojo import main, get_2_max, update


class DojoTest(unittest.TestCase):
    def test_get_2_max(self):
        self.assertEqual(get_2_max([2,7,4,1,8,1]), (4,1))

    def test_get_2_max_2(self):
        self.assertEqual(get_2_max([10,8,7,1]), (0, 1))

    def test_get_2_max_3(self):
        self.assertEqual(get_2_max([4,1,3,2,10]), (0,4))
    
    def test_update_1(self):
        self.assertEqual(update([2,7,4,1,8,1], 4, 1), [2,4,1,1,1])
    
    def test_update_1(self):
        self.assertEqual(update([10,8,7,1], 0, 1), [7,1,2])


if __name__ == '__main__':
    unittest.main()

#lucas - elen - lara - juan - ingrid - ildefonso - sami


# I = [2,7,4,1,8,1]
# O = 1
# I = [10,8,7,1]
# O = 2
# I = [1,4,3,2,10]
# O = 0

