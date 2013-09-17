import unittest
from numeros_romanos import romano_para_decimal

class TestNumerosRomanos(unittest.TestCase):
    
    def teste_i_deve_retorna_1(self):
        saida = romano_para_decimal("I")
        self.assertEqual(saida, 1)

    def teste_iii_deve_retorna_3(self):
        saida = romano_para_decimal("III")
        self.assertEqual(saida, 3)

    def teste_v_deve_retorna_5(self):
        saida = romano_para_decimal("V")
        self.assertEqual(saida, 5)

    def teste_vi_deve_retorna_6(self):
        saida = romano_para_decimal("VI")
        self.assertEqual(saida, 6)

    def teste_XXIII_retorna_23(self):
        self.assertEqual(romano_para_decimal('XXIII'), 23)

    def teste_IX_retorna_9(self):
        self.assertEqual(romano_para_decimal('IX'), 9)

    def teste_XC_retorna_90(self):
        self.assertEqual(romano_para_decimal('XC'), 90)
        
    def teste_XCVIII_retorna_98(self):
        self.assertEqual(romano_para_decimal('XCVIII'), 98)
    
    def test_calcula_romanos_invalidos(self):
        numero_invalido = "IC"
        a = romano_para_decimal(numero_invalido)
        self.assertEqual(a, 99)



unittest.main()