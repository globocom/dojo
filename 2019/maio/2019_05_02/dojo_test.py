import unittest
from dojo import clear_string, calc


class DojoTest(unittest.TestCase):
    def test_clear_space_string_1_plus_1(self):
        self.assertEqual("1+1", clear_string("1 + 1"))

    def test_clear_space_string_1_plus_2(self):
        self.assertEqual("1+2", clear_string("1 + 2"))

    def test_clear_space_string_1_plus_3(self):
        self.assertEqual("1+3", clear_string("1 + 3"))

    def test_clear_parenthesis_string_1_plus_3(self):
        self.assertEqual("1+3", clear_string("(1 + 3"))
    
    def test_clear_parenthesis_string_1_plus_3(self):
        self.assertEqual("1+3", clear_string("(1 + 3)"))

    def test_sum_1_plus_3(self):
        self.assertEqual(4, calc("1+3", "+"))

    def test_sum_2_plus_3(self):
        self.assertEqual(5, calc("2+3", "+"))

    def test_sum_6_plus_10(self):
        self.assertEqual(16, calc("6+10", "+"))

    def test_sum_6_plus_10_plus_4(self):
        self.assertEqual(20, calc("6+10+4", "+"))

    def test_sum_6_plus_10_plus_4(self):
        self.assertEqual(5, calc("10-5", "-"))

    def test_calc_0_minus_5(self):
        self.assertEqual(-5, calc("0-5", "-"))    
if __name__ == '__main__':
    unittest.main()
