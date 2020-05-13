import unittest
from dojo import main


class DojoTest(unittest.TestCase):
    matriz = [
        [1,2],
        [3,1]
        ]
    def test_order_1(self):
        self.assertEqual(main(self.matriz, 1), [[3,1],[1,2]])

    def test_true_2(self):
        self.assertEqual(main(self.matriz, 0), [[1,2],[3,1]])

    def test_true_3(self):
        matriz = [[5,2],[1,4]]
        self.assertEqual(main(matriz, 0), [[1,4],[5,2]])

if __name__ == '__main__':
    unittest.main()



# 1º matriz com os dados dos atletas
# 2º ordenar pelos10 2 #