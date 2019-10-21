import unittest 
from anobissexto import eh_ano_bissexto

class AnoBissextoTest(unittest.TestCase):
	
	def test_1600_eh_bissexto(self):
		self.assertTrue(eh_ano_bissexto(1600))
	
	def test_1601_nao_eh_bissexto(self):
		self.assertFalse(eh_ano_bissexto(1601))
	
	def test_1732_eh_ano_bissexto(self):
		self.assertTrue(eh_ano_bissexto(1732))
		
	def test_1500_nao_eh_bissexto(self):
		self.assertFalse(eh_ano_bissexto(1500))
	
	def test_1888_eh_bissexto(self):
		self.assertTrue(eh_ano_bissexto(1888))

	def test_1944_eh_bissexto(self):
		self.assertTrue(eh_ano_bissexto(1944))
		
	def test_2011_nao_eh_bissexto(self):
		self.assertFalse(eh_ano_bissexto(2011))
		
	def test_9093_nao_eh_bissexto(self):
		self.assertFalse(eh_ano_bissexto(9093))
unittest.main()