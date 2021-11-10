import unittest
from dojo import permutation, hashme


class DojoTest(unittest.TestCase):
    def test_check_permutation_two_numbers(self):
        self.assertEqual(permutation([0,1]),[[0,1],[1,0]])

    def test_check_permutation_one_number(self):
        self.assertEqual(permutation([0]),[[0]])

    def test_check_permutation_no_numbers(self):
        self.assertEqual(permutation([]),[[]])

    def test_check_permutation_three_numbers(self):
        self.assertEqual(hashme(permutation([1,2,3])), hashme([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]))

    def test_check_permutation_four_numbers(self):
        self.assertEqual(
            hashme(permutation([1,2,3,4])),
            hashme([[1,2,3,4],[1,2,4,3],[1,3,2,4],[1,3,4,2],[1,4,2,3],[1,4,3,2],[2,1,3,4],[2,1,4,3],[2,3,1,4],[2,3,4,1],[2,4,1,3],[2,4,3,1],[3,1,2,4],[3,1,4,2],[3,2,1,4],[3,2,4,1],[3,4,1,2],[3,4,2,1],[4,1,2,3],[4,1,3,2],[4,2,1,3],[4,2,3,1],[4,3,1,2],[4,3,2,1]])
        )

if __name__ == '__main__':
    unittest.main()
