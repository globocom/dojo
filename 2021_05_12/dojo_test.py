import unittest
from dojo import main

class DojoTest(unittest.TestCase):
    def test_main(self):
        self.assertTrue(main())



if __name__ == '__main__':
    unittest.main()

# gaus - 1 - 100
#  (a1 + a100) * 100 / 2 = 5050
#  1 2 4 8 -> 1(2^4 - 1)/(2-1) -> formula de uma PG -> no nosso caso a razao é sempre 2 
# a formula fica -> Soma total dos termos = (2^x - 1)
# 7 
# 19 --> 524287 -> 524287/12000 --> 43kg
# 14 --> 1Kg