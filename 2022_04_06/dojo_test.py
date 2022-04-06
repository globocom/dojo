import unittest
from dojo import *

PUZZLE_INPUT = "R5, L2, L1, R1, R3, R3, L3, R3, R4, L2, R4, L4, R4, R3, L2, L1, L1, R2, R4, R4, L4, R3, L2, R1, L4, R1, R3, L5, L4, L5, R3, L3, L1, L1, R4, R2, R2, L1, L4, R191, R5, L2, R46, R3, L1, R74, L2, R2, R187, R3, R4, R1, L4, L4, L2, R4, L5, R4, R3, L2, L1, R3, R3, R3, R1, R1, L4, R4, R1, R5, R2, R1, R3, L4, L2, L2, R1, L3, R1, R3, L5, L3, R5, R3, R4, L1, R3, R2, R1, R2, L4, L1, L1, R3, L3, R4, L2, L4, L5, L5, L4, R2, R5, L4, R4, L2, R3, L4, L3, L5, R5, L4, L2, R3, R5, R5, L1, L4, R3, L1, R2, L5, L1, R4, L1, R5, R1, L4, L4, L4, R4, R3, L5, R1, L3, R4, R3, L2, L1, R1, R2, R2, R2, L1, L1, L2, L5, L3, L1"


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(main())

    def test_parse_1(self):
        self.assertEqual(parse_input("R5"), [("R", 5)])

    def test_parse_2(self):
        self.assertEqual(parse_input("R5, L2"), [("R", 5), ("L", 2)])

    def test_parse_3(self):
        self.assertEqual(parse_input("R5, L2, R22"), [("R", 5), ("L", 2), ("R", 22)])

    def test_walk_1(self):
        self.assertEqual(walk((0, 0, "N"), ("R", 5)), (5, 0, "E"))

    def test_walk_2(self):
        self.assertEqual(walk((0, 0, "N"), ("L", 10)), (-10, 0, "W"))

    def test_walk_3(self):
        self.assertEqual(walk((5, 5, "W"), ("R", 1)), (5, 6, "N"))

    def test_determine_facing_1(self):
        self.assertEqual(determine_facing("N", "R"), "E")

    def test_determine_facing_2(self):
        self.assertEqual(determine_facing("W", "R"), "N")

    def test_determine_facing_3(self):
        self.assertEqual(determine_facing("W", "L"), "S")

    def test_manh_dist_1(self):
        self.assertEqual(manh_dist(4, 6, "R"), 10)

    def test_manh_dist_2(self):
        self.assertEqual(manh_dist(-1, -1, "R"), 2)

    def test_manh_dist_3(self):
        self.assertEqual(manh_dist(-1, 1, "R"), 2)

    def test_aoc_1_1(self):
        self.assertEqual(aoc_1("R2, L3"), 5)

    def test_aoc_1_2(self):
        self.assertEqual(aoc_1("R2, R2, R2"), 2)

    def test_aoc_1_3(self):
        self.assertEqual(aoc_1("R5, L5, R5, R3"), 12)

    def test_aoc_1(self):
        self.assertEqual(aoc_1(PUZZLE_INPUT), 287)

    def test_aoc_2_1(self):
        self.assertEqual(aoc_2("R8, R4, R4, R8"), 4)


# Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
# R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.


if __name__ == "__main__":
    unittest.main()
