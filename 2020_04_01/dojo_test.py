import unittest
from dojo import validate_count_caracters, validate_compare_caracters


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(validate_count_caracters("()"))

    def test_false(self):
        self.assertFalse(validate_count_caracters("([)"))

    def test_false2(self):
        self.assertFalse(validate_count_caracters("([]()"))

    def test_false3(self):
        self.assertFalse(validate_count_caracters("([]()"))

    def test_true2(self):
        self.assertFalse(validate_compare_caracters("("))

    def test_false4(self):
        self.assertTrue(validate_compare_caracters("()"))

    def test_false5(self):
        self.assertTrue(validate_compare_caracters("[]"))

    def test_true3(self):
        self.assertTrue(validate_compare_caracters("{()}"))

if __name__ == '__main__':
    unittest.main()
