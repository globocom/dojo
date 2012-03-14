import unittest

from encontrar_telefone import encontrar_telefone, numeros_por_letras

class EncontrarTelefoneTestCase(unittest.TestCase):

	def test_fora_do_mapeamento_retorna_o_mesmo(self):
		self.assertEqual("0", encontrar_telefone("0"))

	def test_dentro_do_mapeamento_retorna_numero_mapeado(self):
		self.assertEqual(numeros_por_letras['A'], encontrar_telefone("A"))

	def test_composto_dentro_do_mapeamento_retorna_numeros_mapeados(self):
		self.assertEqual('23', encontrar_telefone('AD'))

class MapeamentoDeLetrasTestCase(unittest.TestCase):

	def test_retorna_dois_para_a_letra_a(self):
		self.assertEqual('2', numeros_por_letras['A'])

	def test_retorna_dois_para_a_letra_b(self):
		self.assertEqual('2', numeros_por_letras['B'])

	def test_retorna_dois_para_a_letra_c(self):
		self.assertEqual('2', numeros_por_letras['C'])

	def test_retorna_tres_para_a_letra_d(self):
		self.assertEqual('3', numeros_por_letras['D'])

	def test_retorna_tres_para_a_letra_e(self):
		self.assertEqual('3', numeros_por_letras['E'])

	def test_retorna_tres_para_a_letra_f(self):
		self.assertEqual('3', numeros_por_letras['F'])

	def test_retorna_quatro_para_a_letra_g(self):
		self.assertEqual('4', numeros_por_letras['G'])

	def test_retorna_quatro_para_a_letra_h(self):
		self.assertEqual('4', numeros_por_letras['H'])

	def test_retorna_quatro_para_a_letra_i(self):
		self.assertEqual('4', numeros_por_letras['I'])

	def test_retorna_cinco_para_a_letra_j(self):
		self.assertEqual('5', numeros_por_letras['J'])

	def test_retorna_cinco_para_a_letra_k(self):
		self.assertEqual('5', numeros_por_letras['K'])

	def test_retorna_cinco_para_a_letra_l(self):
		self.assertEqual('5', numeros_por_letras['L'])

	def test_retorna_seis_para_a_letra_m(self):
		self.assertEqual('6', numeros_por_letras['M'])

	def test_retorna_seis_para_a_letra_n(self):
		self.assertEqual('6', numeros_por_letras['N'])

	def test_retorna_seis_para_a_letra_o(self):
		self.assertEqual('6', numeros_por_letras['O'])

	def test_retorna_sete_para_a_letra_p(self):
		self.assertEqual('7', numeros_por_letras['P'])

	def test_retorna_sete_para_a_letra_q(self):
		self.assertEqual('7', numeros_por_letras['Q'])

	def test_retorna_sete_para_a_letra_r(self):
		self.assertEqual('7', numeros_por_letras['R'])

	def test_retorna_sete_para_a_letra_s(self):
		self.assertEqual('7', numeros_por_letras['S'])

	def test_retorna_oito_para_a_letra_t(self):
		self.assertEqual('8', numeros_por_letras['T'])

	def test_retorna_oito_para_a_letra_u(self):
		self.assertEqual('8', numeros_por_letras['U'])

	def test_retorna_oito_para_a_letra_v(self):
		self.assertEqual('8', numeros_por_letras['V'])

	def test_retorna_nove_para_a_letra_w(self):
		self.assertEqual('9', numeros_por_letras['W'])

	def test_retorna_nove_para_a_letra_x(self):
		self.assertEqual('9', numeros_por_letras['X'])

	def test_retorna_nove_para_a_letra_y(self):
		self.assertEqual('9', numeros_por_letras['Y'])

	def test_retorna_nove_para_a_letra_z(self):
		self.assertEqual('9', numeros_por_letras['Z'])

unittest.main()