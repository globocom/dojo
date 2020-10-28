import unittest
from dojo import get_first_diag_points


class DojoTest(unittest.TestCase):
    def test1_get_first_diag_points_(self):
        self.assertEqual(get_first_diag_points([[1,1],[1,1]]), sorted([(0, 0),(0, 1), (1, 0)]))

    def test2_get_first_diag_points_(self):
        self.assertEqual(get_first_diag_points([[3,3,1],[2,2,1]]), sorted([(0, 0),(0, 1), (1, 0), (0, 2)]))

    def test3_get_first_diag_points_(self):
        self.assertEqual(get_first_diag_points([[3,3],[2,2],[1,1]]), sorted([(0, 0),(0, 1),(1, 0),(2,0)]))


if __name__ == '__main__':
    unittest.main()


# Tiago -> Lucas -> Lara -> Sami -> Allan

# def get_first_diag_points(matrix) : lista_dos_inicios_das_diag
# def get_diag(matrix, x, y) : lista_diag
# def make_matrix(matrix, diag, x, y) : matrix_da_lista_de_diag

# [00, 01, 02, 03
#  10, 11, 12, 13
#  20, 21, 22, 23]
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,:2,3,3]]

# diagonal n + m - 1
# tamanho da maior diagonal = número de linhas

#n