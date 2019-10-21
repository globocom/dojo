import unittest
from dojo import Solution


class DojoTest(unittest.TestCase):
    def test_a_a(self):
        solution = Solution()
        self.assertEqual(solution.numJewelsInStones("a","a"), 1)

    def test_a_aa(self):
        solution = Solution()
        self.assertEqual(solution.numJewelsInStones("a","aa"), 2)
    
    def test_a_aaa(self):
        solution = Solution()
        self.assertEqual(solution.numJewelsInStones("a","aaa"), 3)
    
    def test_b_aaa(self):
        solution = Solution()
        self.assertEqual(solution.numJewelsInStones("b","aaa"), 0)
    
    def test_b_aaa(self):
        solution = Solution()
        self.assertEqual(solution.numJewelsInStones("b","aaa"), 0)

if __name__ == '__main__':
    unittest.main()
