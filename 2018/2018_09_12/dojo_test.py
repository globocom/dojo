import unittest
from dojo import calcula_ponto, Jogo, calcula_jogos


class DojoTest(unittest.TestCase):
    def test_team1_victory(self):
        partida = Jogo("flamengo", "vasco", "win")
        self.assertEqual(
            calcula_ponto(partida),
            {"flamengo": 3, "vasco": 0}
        )

    def test_team2_victory(self):
        partida = Jogo("flamengo", "vasco", "loss")
        self.assertEqual(
            calcula_ponto(partida),
            {"flamengo": 0, "vasco": 3}
        )

    def test_draw(self):
        partida = Jogo("flamengo", "madureira", "draw")
        self.assertEqual(
            calcula_ponto(partida),
            {"flamengo": 1, "madureira": 1}
        )

    def test_curitiba_victory(self):
        partida = Jogo("curitiba", "madureira", "win")
        self.assertEqual(
            calcula_ponto(partida),
            {"curitiba": 3, "madureira": 0}
        )

    def test_calcula_jogos(self):
        jogos = [Jogo("curitiba", "madureira", "win"),
                 Jogo("mengao", "vasquim", "win")]
        self.assertEqual(
            calcula_jogos(jogos),
            {"curitiba": 3, "madureira": 0, "mengao": 3, "vasquim": 0}
        )

    def test_calcula_jogos2(self):
        jogos = [Jogo("curitiba", "madureira", "win"),
                 Jogo("mengao", "vasquim", "win"),
                 Jogo("vascao", "gremio", "draw")]
        self.assertEqual(
            calcula_jogos(jogos),
            {"curitiba": 3, "madureira": 0, "mengao": 3,
                "vasquim": 0, "vascao": 1, "gremio": 1}
        )

    def test_calcula_jogos3(self):
        jogos = [Jogo("curitiba", "madureira", "win"),
                 Jogo("mengao", "vasquim", "loss"),
                 Jogo("vascao", "gremio", "draw")]
        self.assertEqual(
            calcula_jogos(jogos),
            {["curitiba": 3, "madureira": 0, "mengao": 0,
                "vasquim": 3, "vascao": 1, "gremio": 1]}
        )


if __name__ == '__main__':
    unittest.main()
