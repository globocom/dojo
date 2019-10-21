import unittest
from caixa import Caixa, ValorNaoPermitido

class CaixaEletronicoTest(unittest.TestCase):
    
    def setUp(self):
        self.caixa = Caixa()
        
    def test_pobrinho_quer_sacar_10_reais(self):
        self.assertEqual(self.caixa.sacar(10), [10,])
    
    def test_menos_pobrinho_quer_sacar_20_reais(self):
        self.assertEqual(self.caixa.sacar(20), [20,])
    
    def test_classe_media_quer_sacar_50_reais(self):
        self.assertEqual(self.caixa.sacar(50), [50,])
    
    def test_rico_quer_sacar_100_reais(self):
        self.assertEqual(self.caixa.sacar(100), [100,])
    
    def test_sacar_30_reais(self):
        self.assertEqual(self.caixa.sacar(30), [20, 10])
    
    def test_sacar_130_reais(self):
        self.assertEqual(self.caixa.sacar(130), [100, 20, 10])
        
    def test_sacar_280_reais(self):
        self.assertEqual(self.caixa.sacar(280), [100, 100, 50, 20, 10])
        
    def test_sacar_15_reais(self):
        try:
            self.caixa.sacar(15)
        except ValorNaoPermitido:
            return
        
        assert False
    
    def test_zacarias_quer_sacar_menos_200_reais(self):
        try:
            self.caixa.sacar(-200)
        except ValorNaoPermitido:
            return
        
        assert False
        
    def test_contar_quando_houver_2_notas_de_100(self):
        self.assertEqual(self.caixa.como_dicionario([100, 100]), {100 : 2})

    def test_contar_quando_houver_2_notas_de_100_e_1_de_50(self):
        self.assertEqual(self.caixa.como_dicionario([100, 100, 50]), {100: 2, 50: 1})
    
    def test_contar_quando_houver_2_notas_de_100_e_1_de_50_e_2_de_20(self):
        self.assertEqual(self.caixa.como_dicionario([100, 100, 50, 20, 20]), {100: 2, 50: 1, 20: 2})
            
    
unittest.main()
        

