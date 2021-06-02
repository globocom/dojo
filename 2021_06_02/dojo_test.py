import unittest
from dojo import main


class DojoTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(main("aaca", "aba", "aabaaca"))
    def test_2(self):
        self.assertTrue(main("aabcc", "dbbca", "aadbbcbcac"))
    def test_3(self):
        self.assertFalse(main("aabcc", "dbbca", "aadbbbaccc"))



if __name__ == '__main__':
    unittest.main()


# Tiago - Lara - Elen - João - Ingrid - Ildefonso