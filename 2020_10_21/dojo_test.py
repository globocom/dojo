import unittest
from dojo import is_decreasing, is_increasing, main


class DojoTest(unittest.TestCase):
    def test_decreasing_1(self):
        self.assertTrue(is_decreasing(3, 2, 1))
    
    def test_decreasing_2(self):
        self.assertFalse(is_decreasing(1, 2, 3))

    def test_decreasing_3(self):
        self.assertTrue(is_decreasing(4, 3, 1))

    def test_increasing_1(self):
        self.assertFalse(is_increasing(4, 3, 1))

    def test_increasing_2(self):
        self.assertTrue(is_increasing(8, 9, 10))

    def test_increasing_3(self):
        self.assertTrue(is_increasing(1, 2, 3))

    def test_main_1(self):
        self.assertEqual(main([1, 2, 3, 4]),4)

    def test_main_2(self):
        self.assertEqual(main([2,5,3,4,1]),3)
    
    def test_main_3(self):
        self.assertEqual(main([2,1,3]),0)

if __name__ == '__main__':
    unittest.main()

# Elen - Ingrid - Sami - Lucas - Lara - Juan - Mateus

# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. 
# (2,3,4), (5,4,1), (5,3,1). 

#Input: rating = [2,1,3]
#Output: 0


