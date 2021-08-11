import unittest
from dojo import *


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(main())

    def test_unidade_1(self):
        self.assertEqual(unidade(9), "IX")

    def test_unidade_2(self):
        self.assertEqual(unidade(5), "V")

    def test_unidade_3(self):
        self.assertEqual(unidade(0), "")

    def test_dezena_1(self):
        self.assertEqual(dezena(9), "XC")

    def test_dezena_2(self):
        self.assertEqual(dezena(5), "L")

    def test_dezena_3(self):
        self.assertEqual(dezena(0), "")

    def test_centena_1(self):
        self.assertEqual(centena(9), "CM")

    def test_centena_2(self):
        self.assertEqual(centena(5), "D")

    def test_centena_3(self):
        self.assertEqual(centena(0), "")

    def test_milhares_1(self):
        self.assertEqual(milhares(1), "M")

    def test_milhares_2(self):
        self.assertEqual(milhares(3), "MMM")

    def test_milhares_3(self):
        self.assertEqual(milhares(0), "")

    def test_solver_1(self):
        self.assertEqual(solver(58), "LVIII")

    def test_solver_2(self):
        self.assertEqual(solver(9), "IX")

    def test_solver_3(self):
        self.assertEqual(solver(3999), "MMMCMXCIX")


if __name__ == "__main__":
    unittest.main()


# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


# decimal - 40
# XXXX -- XL

# 659 seiscentos e cinquenta e nove
# 9 5 6
# 9 -> IX
# 5 -> L
# 6 -> DC
# func -> 9 5 6 -- centena 3

# unidades(9) -> "IX"
# dezenas(5)  -> "L"
# centenas(6) -> "DC"
# milhares(0) -> ""
