import unittest
from dojo import roman_to_int, get_numbers, calc


class DojoTest(unittest.TestCase):
    def test_i(self):
        self.assertEqual(roman_to_int("I"), 1)

    def test_v(self):
        self.assertEqual(roman_to_int("V"), 5)

    def test_x(self):
        self.assertEqual(roman_to_int("X"), 10)

    def test_vi(self):
        self.assertEqual(get_numbers("VI"), [5, 1])

    def test_vii(self):
        self.assertEqual(get_numbers("VII"), [5, 1, 1])

    def test_vi(self):
        self.assertEqual(get_numbers("VIII"), [5, 1, 1, 1])

    def test_check_main(self):
        self.assertEqual(calc([5, 1]), 6)

    def test_check_main_tree_args(self):
        self.assertEqual(calc([5, 1, 1]), 7)

    def test_check_main_four_args(self):
        self.assertEqual(calc([1, 5]), 4)


if __name__ == "__main__":
    unittest.main()
