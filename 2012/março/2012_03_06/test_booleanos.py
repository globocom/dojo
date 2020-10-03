import unittest

from booleanos import parsear_booleano


class BooleanosTestCase(unittest.TestCase):

	def test_quando_a_expressao_eh_true_o_resultado_eh_true(self):
		self.assertEqual(True, parsear_booleano("true"))

	def test_quando_a_expressao_e_false_o_resultado_e_false(self):
		self.assertEqual(False, parsear_booleano("false"))

	def test_quando_a_expressao_eh_true_e_true_return_true(self):
		self.assertEqual(True, parsear_booleano("true and true"))

	def test_quando_a_expressao_eh_false_e_false_return_false(self):
		self.assertEqual(False, parsear_booleano("false and false"))

	def test_quando_a_expressao_eh_false_e_true_return_false(self):
		self.assertEqual(False, parsear_booleano("false and true"))

	def test_quando_a_expressao_eh_false_ou_false_return_false(self):
		self.assertEqual(False, parsear_booleano("false or false"))

	def test_quando_a_expressao_eh_true_ou_true_return_true(self):
		self.assertEqual(True, parsear_booleano("true or true"))

	def test_quando_a_expressao_eh_true_ou_false_return_true(self):
		self.assertEqual(True, parsear_booleano("true or false"))

	def test_quando_a_expressao_eh_true_xor_false_return_true(self):
		self.assertEqual(True, parsear_booleano("true xor false"))

	def test_quando_a_expressao_eh_true_xor_true_return_false(self):
		self.assertEqual(False, parsear_booleano("true xor true"))

	def test_quando_a_expressao_e_false_xor_false_return_false(self):
		self.assertEqual(False, parsear_booleano("false xor false"))

	def test_quando_a_expressao_e_true_xor_true_xor_true_return_true(self):
		self.assertEqual(True, parsear_booleano("true xor true xor true"))

	def test_quando_a_expressao_e_true_and_true_xor_false_return_true(self):
		self.assertEqual(True, parsear_booleano("true and true xor false"))

unittest.main()