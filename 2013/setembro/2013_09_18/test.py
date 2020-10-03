import unittest

from Cheque_por_extenso import convert


class ChequeExtensoTestCase(unittest.TestCase):

    def test_receive_1_return_um_real(self):
        self.assertEqual(convert(1.00), "um real")

    def test_receive_2_return_dois_reais(self):
        self.assertEqual(convert(2.00),"dois reais")
        
    def test_receive_10_return_dez_centavos(self):
        self.assertEqual(convert(0.10),"dez centavos")

    def test_receive_2_10_return_dois_reais_e_10_centavos(self):
        self.assertEqual(convert(2.10),"dois reais e dez centavos")        
    
unittest.main()