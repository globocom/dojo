
import unittest
from expressao_matematica import expressao_matematica

class ExpressaoNumericaTestCase(unittest.TestCase):
    
    def test_leitura_de_um_numero_de_um_digito(self):
        self.assertEquals(expressao_matematica('1'), 1)
        self.assertEquals(expressao_matematica('2'), 2)
    
    def test_soma_com_um_digito(self):
        self.assertEquals(expressao_matematica('1+1'), 2)
        self.assertEquals(expressao_matematica('1+2'), 3)

    def test_soma_com_dois_digitos(self):
        self.assertEquals(expressao_matematica('1+11'), 12)
        self.assertEquals(expressao_matematica('10+11'), 21)
        
    def test_soma_com_espaco(self):
        self.assertEquals(expressao_matematica('10 + 3'), 13)

    def test_soma_com_tres_numeros(self):
        self.assertEquals(expressao_matematica('10 + 3 + 4'), 17)

    def test_subtracao_um_digito(self):
        self.assertEquals(expressao_matematica('2-1'), 1)
    
    def test_subtracao_dois_digitos(self):
        self.assertEquals(expressao_matematica('12-1'), 11)
    
    def test_subtracao_tres_digitos(self):
        self.assertEquals(expressao_matematica('12-2-1'), 9)

    def test_soma_1_mais_1_e_subtrai_1(self):
       self.assertEquals(expressao_matematica('1+1-1'), 1)

    def test_subtrai_1_de_1_e_soma_1(self):
       self.assertEquals(expressao_matematica('1-1+1'), 1)

    def test_multiplics_2_por_2(self):
       self.assertEquals(expressao_matematica('2*2'), 4)
if __name__ == '__main__':
    unittest.main()
