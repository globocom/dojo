import unittest
from dojo import tem_bomba_direita, tem_bomba_esquerda, tem_bomba_acima, conta_bombas


class DojoTest(unittest.TestCase):
    def test_tem_bomba_direita(self):
        board = [".", ".", "*", "."]
        self.assertFalse(tem_bomba_direita(board, 0))
        self.assertTrue(tem_bomba_direita(board, 1))
        self.assertFalse(tem_bomba_direita(board, 2))
        self.assertFalse(tem_bomba_direita(board, 3))

    def test_tem_bomba_esquerda(self):
        board = [".", ".", "*", "*"]
        self.assertTrue(tem_bomba_esquerda(board, 3))
        self.assertFalse(tem_bomba_esquerda(board, 2))
        self.assertFalse(tem_bomba_esquerda(board, 1))
        self.assertFalse(tem_bomba_esquerda(board, 0))

    def test_conta_bombas(self):
        board = [".", "*", ".", "*", ".", "."]
        self.assertEqual(1, conta_bombas(board, 0))
        self.assertEqual(2, conta_bombas(board, 2))
        self.assertEqual(1, conta_bombas(board, 4))
        self.assertEqual(0, conta_bombas(board, 5))
        self.assertEqual(-1, conta_bombas(board, 1))

    def test_tem_bomba_acima(self):
        board = [["."],
                 ["*"],
                 ["."],
                 ["*"],
                 ["."],
                 ["."]]
        self.assertTrue(tem_bomba_acima(board, 0, 2))
        self.assertFalse(tem_bomba_acima(board, 0, 1))


if __name__ == '__main__':
    unittest.main()
