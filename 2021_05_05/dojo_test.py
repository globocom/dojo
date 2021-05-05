import unittest
from dojo import main, opposite_directions


class DojoTest(unittest.TestCase):
    def test_opposite_directions(self):
        self.assertFalse(opposite_directions("NORTH","NORTH"))

    def test_opposite_directions4(self):
        cases = ["NORTH", "WEST", "EAST", "SOUTH"]
        for i, case in enumerate(cases):
            self.assertTrue(opposite_directions(case,cases[-i-1]))

    def test_main1(self):
        self.assertListEqual(main(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ["WEST"])
    def test_main2(self):
        self.assertListEqual(main(["NORTH", "WEST", "SOUTH", "EAST"] ), ["NORTH", "WEST", "SOUTH", "EAST"] )
    def test_main3(self):
        self.assertListEqual(main(["SOUTH", "EAST", "WEST", "NORTH"]), [] )

if __name__ == '__main__':
    unittest.main()



# Ordem: Sami, Lara, Tiago
# "NORTH", "EAST", "WEST", "SOUTH".
# 