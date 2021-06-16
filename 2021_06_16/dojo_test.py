import unittest
from dojo import main, sum_opposites

class DojoTest(unittest.TestCase):
    def test_sum_opposites_1(self):
        self.assertEqual(sum_opposites([2, 3, 3, 5], 0), 7)
    def test_sum_opposites_2(self):
        self.assertEqual(sum_opposites([2, 3, 3, 5], 1), 6)
    def test_sum_opposites_3(self):
        self.assertEqual(sum_opposites([2, 3, 4, 4, 5 ,6], 2), 8)

    def test_main_1(self):
        self.assertEqual(main([2, 3, 3, 5]), 7)
    def test_main_2(self):
        self.assertEqual(main([3, 5, 4, 2, 4, 6]), 8)
    def test_main_3(self):
        self.assertEqual(main([3, 5, 2, 3]), 7)


if __name__ == '__main__':
    unittest.main()


# [3,5,2,3]
# [2, 3, 3, 5]

#[3,5,4,2,4,6]
# [2, 3, 4, 4, 5 ,6]

# - sort array
# - pair leftmost+rightmost
#   - save sum if greatest
# - return max sum

#