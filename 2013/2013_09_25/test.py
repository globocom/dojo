import unittest

from battleship import Jogo


class BattleshipTest(unittest.TestCase):

    def test_cria_tabuleiro(self):
        jogo = Jogo()
        self.assertEquals(len(jogo.tab), 5)
        self.assertEquals(len(jogo.tab[0]), 5)

    def test_tabuleiro_tem_apenas_um_barco(self):
        jogo = Jogo()
        x, y = jogo.coloca_navio()
        self.assertTrue(x >= 0 and x < 5)
        self.assertTrue(y >= 0 and y < 5)

    def test_player_erra(self):
        jogo = Jogo()
        jogo.resposta = (0, 0)
        jogo.joga(1, 2)
        self.assertEquals(jogo.tab[1][2], 'x')

unittest.main()
