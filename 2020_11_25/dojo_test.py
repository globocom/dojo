import unittest
from dojo import comp_char, solve


class DojoTest(unittest.TestCase):
    def test_compchar_1(self):
        self.assertFalse(comp_char('e', 'd'))

    def test_compchar_2(self):
        self.assertTrue(comp_char('d', 'd'))

    def test_compchar_3(self):
        self.assertTrue(comp_char('e', 'e'))

    def test_solve(self):
        self.assertEqual(solve("etda", "date"), ("IIIRIRRR", True))

    def test_solve2(self):
        self.assertEqual(solve("ostap", "patos"), ("IIIIIRRR", False))

    def test_solve3(self):
        self.assertEqual(solve("abdcba", "abcbad"), ("IRIRIIRIRIRR", True))


if __name__ == '__main__':
    unittest.main()
