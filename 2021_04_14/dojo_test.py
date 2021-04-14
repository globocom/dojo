import unittest
from dojo import main


class DojoTest(unittest.TestCase):
    def test_zero(self):
        primes_list = list(primes(0))
        self.assertListEqual(primes_list, [])

    def test_one(self):
        primes_list = list(primes(3))
        self.assertListEqual(primes_list, [2])

    def test_two(self):
        primes_list = list(primes(12))
        self.assertListEqual(primes_list, [2,3,5,7,11])


if __name__ == '__main__':
    unittest.main()
