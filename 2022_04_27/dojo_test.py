import unittest
from dojo import *

EXAMPLE_INPUT = """
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
""".strip()

class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(main())

    def test_split_string_1(self):
        self.assertEqual(split_string("aaaaa-bbb-z-y-x-123[abxyz]"), ("aaaaa-bbb-z-y-x", 123, "abxyz"))

    def test_split_string_2(self):
        self.assertEqual(split_string("a-b-c-d-e-f-g-h-987[abcde]"), ("a-b-c-d-e-f-g-h", 987, "abcde"))

    def test_split_string_3(self):
        self.assertEqual(split_string("not-a-real-room-404[oarel]"), ("not-a-real-room", 404, "oarel"))

    def test_split_string_1(self):
        self.assertEqual(split_string("totally-real-room-200[decoy]"), ("totally-real-room", 200, "decoy"))

    def test_count_letter_1(self):
        self.assertEqual(count_letter("aaaaa-bbb-z-y-x"), {"a": 5, "b": 3, "z": 1, "y": 1, "x": 1})

    def test_checksum_from_count_1(self):
        self.assertEqual(checksum_from_count({"a": 5, "b": 3, "z": 1, "y": 1, "x": 1}), "abxyz")

    def test_checksum_from_count_2(self):
        self.assertEqual(checksum_from_count({"a": 1, "b": 1, "z": 4, "y": 1, "x": 1}), "zabxy")

    def test_checksum_from_count_3(self):
        self.assertEqual(checksum_from_count({"a": 5, "b": 5, "c":1, "z": 4, "y": 1, "x": 1}), "abzcx")


    def test_compute_checksum_1(self):
        self.assertEqual(compute_checksum("aaaaa-bbb-z-y-x"), "abxyz")
    
    def test_compute_checksum_2(self):
        self.assertEqual(compute_checksum("a-b-c-d-e-f-g-h"), "abcde")
    
    def test_compute_checksum_3(self):
        self.assertEqual(compute_checksum("not-a-real-room"), "oarel")

    def test_aoc_day_one_1(self):
        self.assertEqual(aoc_day_one(EXAMPLE_INPUT), 1514)

    def test_aoc_day_one_real(self):
        with open("input.txt") as f:
            input = f.read().strip()
        self.assertEqual(aoc_day_one(input), 137896)

    def test_shift_name_1(self):
        self.assertEqual(shift_name("qzmt-zixmtkozy-ivhz", 343), "very encrypted name")

    def test_aoc_day_two_1(self):
        with open("input.txt") as f:
            input = f.read().strip()
        self.assertEqual(aoc_day_two(input), 501)
        
if __name__ == '__main__':
    unittest.main()
