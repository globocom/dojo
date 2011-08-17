# coding: utf-8

import unittest
from codigo import preencha_cheque

class TestCheque(unittest.TestCase):
    
    def test_cheque_somente_com_reais(self):
        self.assertEquals(preencha_cheque(1.00), "um real")
        self.assertEquals(preencha_cheque(2.00), "dois reais")
        self.assertEquals(preencha_cheque(3.00), "três reais")
        self.assertEquals(preencha_cheque(4.00), "quatro reais")
        self.assertEquals(preencha_cheque(5.00), "cinco reais")
        self.assertEquals(preencha_cheque(6.00), "seis reais")
        self.assertEquals(preencha_cheque(7.00), "sete reais")
        self.assertEquals(preencha_cheque(8.00), "oito reais")
        self.assertEquals(preencha_cheque(9.00), "nove reais")

    
    def test_cheque_cinquenta_centavos(self):
        self.assertEquals(preencha_cheque(0.50), 'cinquenta centavos')

    def test_cheque_dez_reais(self):
        self.assertEqual(preencha_cheque(10.00), "dez reais")
    
    def test_cheque_maiores_que_dez_e_menor_que_vinte(self):
        self.assertEqual(preencha_cheque(11.00), "onze reais")
        self.assertEqual(preencha_cheque(12.00), "doze reais")
        self.assertEqual(preencha_cheque(13.00), "treze reais")
        self.assertEqual(preencha_cheque(14.00), "catorze reais")
        self.assertEqual(preencha_cheque(15.00), "quinze reais")
        self.assertEqual(preencha_cheque(16.00), "dezesseis reais")
        self.assertEqual(preencha_cheque(17.00), "dezessete reais")
        self.assertEqual(preencha_cheque(18.00), "dezoito reais")
        self.assertEqual(preencha_cheque(19.00), "dezenove reais")
        
    def test_cheque_vinte_reais(self):
        self.assertEqual(preencha_cheque(20.00), "vinte reais")
    
    def test_vinte_quatro_reais(self):
        self.assertEquals(preencha_cheque(24.00), "vinte e quatro reais")
        
    def test_trinta_reais(self):
        self.assertEquals(preencha_cheque(30.00), 'trinta reais')

unittest.main()