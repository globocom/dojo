import unittest
from caixa_eletronico import sacar, imprime_sacar


class TestCase(unittest.TestCase):

	def test_sacar_10_retorna_uma_nota_de_10(self):
		self.assertEqual(sacar(10), {10: 1})

	def test_sacar_20_retorna_uma_nota_de_20(self):
		self.assertEqual(sacar(20), {20: 1})

	def test_sacar_30_retorna_1_de_10_e_1_de_20(self):
		self.assertEqual(sacar(30), {10: 1, 20: 1})

	def test_sacar_40_retorna_2_de_20(self):
		self.assertEqual(sacar(40), {20: 2})

	def test_sacar_5_retorna_erro(self):
		with self.assertRaises(Exception) as e:
			sacar(5)
			self.assertEqual(e.message, "valor indisponivel")

	def test_sacar_370_retorna_3_de_100_1_de_50_e_uma_de_vinte_reais(self):
		self.assertEqual(sacar(370),{100: 3, 50: 1, 20: 1})

	def test_texto_de_retorno_ao_sacar_10(self):
		self.assertEqual(imprime_sacar(10), "Entregar 1 nota de R$10,00")

	def test_text_de_retorno_ao_sacar_30(self):
		self.assertEqual(imprime_sacar(30), "Entregar 1 nota de R$20,00 e 1 nota de R$10,00")

unittest.main()