import unittest
from dojo import *


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(main())

    def teste_split_string1(self):
        self.assertEqual(split_string("1 2 3"), [1, 2, 3]) 
    def teste_split_string2(self):
        self.assertEqual(split_string("-1 2 -33"), [-1, 2, -33]) 
    def teste_split_string3(self):
        self.assertEqual(split_string("0 2 99999"), [0, 2, 99999]) 

    def teste_find_max1(self):
        self.assertEqual(find_max([1, 2, 3]), 3)
    def teste_find_max2(self):
        self.assertEqual(find_max([1, 0, 7]), 7)
    def teste_find_max3(self):
        self.assertEqual(find_max([7,-5, 3]), 7)

    def test_find_min1(self):
        self.assertEqual(find_min([1, 2, 3]), 1)
    def test_find_min2(self):
        self.assertEqual(find_min([8, 2, 5]), 2)
    def test_find_min3(self):
        self.assertEqual(find_min([5, 6, 4]), 4)

    def test_ans1(self):
        self.assertEqual(ans(5, 9), "9 5")
    def test_ans2(self):
        self.assertEqual(ans(10, 20), "20 10")
    def test_ans3(self):
        self.assertEqual(ans(-100, 220), "220 -100")

    def test_high_and_low1(self):
        self.assertEqual(high_and_low("1 2 3 4 5"), "5 1")
    def test_high_and_low2(self):
        self.assertEqual(high_and_low("1 2 -3 4 5"), "5 -3")
    def test_high_and_low3(self):
        self.assertEqual(high_and_low("1 9 3 4 -5"), "9 -5")

# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"



if __name__ == '__main__':
    unittest.main()



# Lara
# Leo - He's back!  (:
# tcarreira
# Willian
# Christian
# Paulo
# Nicolas
# Rogerio dos Anjos  - Skip me.  (: