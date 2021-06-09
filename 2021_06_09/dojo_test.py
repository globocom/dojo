import unittest
from dojo import move_zeroes, valid_sudoku, validate_rows

class DojoTest(unittest.TestCase):
    def test_move_zeroes_1(self):
        self.assertEqual(move_zeroes([0,1,0,3,12]), [1,3,12,0,0])
    def test_move_zeroes_2(self):
        self.assertEqual(move_zeroes([0,1,3,12]), [1,3,12,0])
    def test_move_zeroes_3(self):
        self.assertEqual(move_zeroes([1,3,12]), [1,3,12])
    def test_valid_sudoku_1(self):
        board = [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        self.assertTrue(validate_rows(board))
    def test_valid_sudoku_2(self):
        board = [["8","3","3",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        self.assertFalse(validate_rows(board))    

    def test_valid_sudoku_3(self):
        board = [["9","9",]
                ,["6",".",]]
        self.assertFalse(validate_rows(board))     

if __name__ == '__main__':
    unittest.main()

# Ingrid - Nicolas - Juan

# Problema 1:

# input = [0,1,0,3,12]
# output = [1,3,12,0,0]

# passar pelo array
# se for zero a gente remove e adicionar +1 no contador
# se n segue a vida
# no final nós concatenamos um array de 0 com a quantidade do contador

# Problema 2:

# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

# True

# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

# False

# Testa cada linha
    # Se em algum momento n estiver válido => retorna False
# Testa cada coluna
    # Se em algum momento n estiver válido => retorna False
# Testa os blocos