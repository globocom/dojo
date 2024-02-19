import unittest
from codigo import *

class TestCollatz(unittest.TestCase):

	def test_de_2_deve_retornar_2_numeros(self):
		self.assertEqual(collatz(2), 2)
		
	def test_de_4_deve_retornar_3_numeros(self):
		self.assertEqual(collatz(4), 3)
		
	def test_8_retorna_4(self):
		self.assertEqual(collatz(8), 4)
		
	def test_1_retorna_1(self):
		self.assertEqual(collatz(1), 1)
		
	def test_5_retorna_6(self):
		self.assertEqual(collatz(5), 6)

	def test_7_retorna_16(self):
		self.assertEqual(collatz(7), 17)
		
	def test_de_1_ate_10(self):
		self.assertEqual(maior_de_todos(10), 20)
		
unittest.main()