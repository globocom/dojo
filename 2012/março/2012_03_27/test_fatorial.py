import unittest

from fatorial import fatorial

class FatorialTestCase(unittest.TestCase):

    def test_fatorial_1_1(self):
        self.assertEqual(1, fatorial(1, 1))

    def test_fatorial_2_1(self):
        self.assertEqual(2, fatorial(2, 1))

    def test_fatorial_3_1(self):
        self.assertEqual(6, fatorial(3, 1))

    def test_fatorial_4_1(self):
        self.assertEqual(24, fatorial(4, 1))

    def test_fatorial_10_3(self):
        self.assertEqual(280, fatorial(10, 3))

    def test_fatorial_21_19(self):
        self.assertEqual(42, fatorial(21, 19))

unittest.main()
