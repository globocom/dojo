import unittest
from dojo import combinations


class DojoTest(unittest.TestCase):
    def test_amount_1(self):
        coins = [1]
        amount = 1
        self.assertEqual(combinations(coins, amount), 1)

    def test_amount_2(self):
        coins = [1]
        amount = 2
        self.assertEqual(combinations(coins, amount), 2)

    def test_amount_3(self):
        coins = [1]
        amount = 3
        self.assertEqual(combinations(coins, amount), 3)

    def test_amount_11(self):
        coins = [5, 2, 1]
        amount = 11
        self.assertEqual(combinations(coins, amount), 3)

    def test_amount_3_2(self):
        coins = [5, 2]
        amount = 3
        self.assertEqual(combinations(coins, amount), -1)


if __name__ == '__main__':
    unittest.main()
