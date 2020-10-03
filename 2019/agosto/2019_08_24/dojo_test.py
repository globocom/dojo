import unittest
from dojo import sum, sub, mult, div, calc


class DojoTest(unittest.TestCase):
    def test_sum_1_and_2(self):
        self.assertEqual(sum(1,2),3)

    def test_sum_n1_and_5(self):
        self.assertEqual(sum(-1,5),4)

    def test_sum_n1_and_5(self):
        self.assertEqual(sum(0,0),0)
    
    def test_sub_1_and_2(self):
        self.assertEqual(sub(1,2),-1)

    def test_sub_n1_and_2(self):
        self.assertEqual(sub(-1,2),-3)

    def test_sub_0_and_0(self):
        self.assertEqual(sub(0,0),0)

    def test_mult_1_and_2(self):
        self.assertEqual(mult(1,2),2)

    def test_mult_n1_and_5(self):
        self.assertEqual(mult(-1,5),-5)

    def test_mult_0_and_0(self):
        self.assertEqual(mult(0,0),0)

    def test_div_1_and_2(self):
        self.assertEqual(div(1,2), 0.5)

    def test_div_n1_and_4(self):
        self.assertEqual(div(-1,4), -0.25)

    def test_div_0_and_1(self):
        self.assertEqual(div(0,1),0)

    def test_calc_4_and_2(self):
        self.assertEqual(calc(4,2),[6,2,8,2])

    def test_calc_n1_and_4(self):
        self.assertEqual(calc(-1,4),[3,-5,-4,-0.25])

    def test_calc_0_and_1(self):
        self.assertEqual(calc(0,1),[1,-1,0,0])

if __name__ == '__main__':
    unittest.main()
