import unittest
from jokenpo import jokenpo, papel, tesoura, pedra


class TestJokenpo(unittest.TestCase):

    def test_pedra_e_pedra(self):
        resposta = jokenpo(pedra, pedra)
        self.assertEqual(resposta, "pedra empata com pedra")

    def test_pedra_e_tesoura(self):
        resposta = jokenpo(pedra, tesoura)
        self.assertEqual(resposta, "pedra ganha de tesoura")

    def test_tesoura_e_pedra(self):
        resposta = jokenpo(tesoura, pedra)
        self.assertEqual(resposta, "pedra ganha de tesoura")

    def test_pedra_e_papel(self):
        resposta = jokenpo(pedra, papel)
        self.assertEqual(resposta, "papel ganha de pedra")
    
    def test_pedra_ganha_tesoura_model(self):
        self.assertEqual(pedra.ganha_de, tesoura)

    def test_tesoura_ganha_papel_model(self):
        self.assertEqual(tesoura.ganha_de, papel)

    def test_papel_ganha_pedra_model(self):
        self.assertEqual(papel.ganha_de, pedra)
if __name__ == "__main__":
    unittest.main()