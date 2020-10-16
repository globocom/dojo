import unittest
from dojo import is_substring_valid, main

class DojoTest(unittest.TestCase):
    def test_is_substring_valid_1(self):
        self.assertTrue(is_substring_valid("LR"))

    def test_is_substring_valid_2(self):
        self.assertFalse(is_substring_valid("LRR"))
    
    def test_is_substring_valid_3(self):
        self.assertTrue(is_substring_valid("LLRR"))

    def test_main(self):
        self.assertEqual(main("LLRR"), 1)

    def test_main_2(self):
        self.assertEqual(main("LLRRLR"), 2)

    def test_main_3(self):
        self.assertEqual(main("LLRRLRLR"), 3)

    def test_main_4(self):
        self.assertEqual(main("LRLRLRLRLLRR"), 5)


if __name__ == '__main__':
    unittest.main()

# Sami - Juan - Lucas - Elen – Pri – Thiago – Vierno – Santana – Ingrid - Natalia

# RLRRLLRLRL
# RL LLLRRR LR
# LLLLRRRR 
# RLRRRLLRLL            