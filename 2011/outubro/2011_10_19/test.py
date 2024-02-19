import unittest
from codigo import menor_numero_divisivel

class Problem5EulerTestCase(unittest.TestCase):

    def test_menor_numero_divisivel_pelos_numeros_de_1_a_1(self):
        self.assertEqual(1, menor_numero_divisivel(1))

    def test_menor_numero_divisivel_pelos_numeros_de_1_a_2(self):
        self.assertEqual(2, menor_numero_divisivel(2))

    def test_menor_numero_divisivel_pelos_numeros_de_1_a_3(self):
        self.assertEqual(6, menor_numero_divisivel(3))

    def test_menor_numero_divisivel_pelos_numeros_de_1_a_10(self):
        self.assertEqual(2520, menor_numero_divisivel(10))

    def test_menor_nemero_divisivel_pelos_numeros_de_1_a_20(self):
        self.assertEqual(232792560, menor_numero_divisivel(20))



unittest.main()
