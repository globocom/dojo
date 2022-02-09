import unittest
from dojo import *

mini_test = """
2x3x4
1x1x10
""".strip()


class DojoTest(unittest.TestCase):
    def test_parse_present_1(self):
        self.assertEqual(parse_present("2x3x4"), [2, 3, 4])

    def test_parse_present_2(self):
        self.assertEqual(parse_present("5x6x7"), [5, 6, 7])

    def test_parse_present_3(self):
        self.assertEqual(parse_present("1x1x10"), [1, 1, 10])

    def test_calculate_areas_1(self):
        self.assertEqual(calculate_areas([2, 3, 4]), [6, 12, 8])

    def test_calculate_areas_2(self):
        self.assertEqual(calculate_areas([1, 1, 10]), [1, 10, 10])

    def test_get_min_area_1(self):
        self.assertEqual(get_min_area([6, 12, 8]), 6)

    def test_get_min_area_2(self):
        self.assertEqual(get_min_area([1, 10, 10]), 1)

    def test_get_present_area_1(self):
        self.assertEqual(get_present_area([2, 3, 4]), 58)

    def test_get_present_area_2(self):
        self.assertEqual(get_present_area([1, 1, 10]), 43)

    def test_main(self):
        self.assertEqual(main(mini_test), 101)


if __name__ == "__main__":
    unittest.main()
