import unittest
from codigo import palavra_eh_primo, num_eh_primo

class TestPalavraPrimo(unittest.TestCase):
    
    def test_a_nao_deve_ser_primo(self):
        self.assertFalse(palavra_eh_primo('a'))
        
    def test_b_deve_ser_primo(self):
        self.assertTrue(palavra_eh_primo('b'))
        
    def test_c_deve_ser_primo(self):
        self.assertTrue(palavra_eh_primo('c'))
        
    def test_d_nao_deve_ser_primo(self):
        self.assertFalse(palavra_eh_primo('d'))
    
    def test_aa_deve_ser_primo(self):
        self.assertTrue(palavra_eh_primo('aa'))
    
    def test_ab_deve_ser_primo(self):
        self.assertTrue(palavra_eh_primo('ab'))

    def test_abc_nao_deve_ser_primo(self):
        self.assertFalse(palavra_eh_primo('abc'))
        
    def test_A_nao_deve_ser_primo(self):
        self.assertFalse(palavra_eh_primo('A'))

class TestNumeroEhPrimo(unittest.TestCase):
    
    def test_0_nao_eh_primo(self):
        self.assertFalse(num_eh_primo(0))
        
    def test_1_nao_eh_primo(self):
        self.assertFalse(num_eh_primo(1))
        
    def test_2_eh_primo(self):
        self.assertTrue(num_eh_primo(2))
    
    def test_4_nao_eh_primo(self):
        self.assertFalse(num_eh_primo(4))
        
    def test_13_eh_primo(self):
        self.assertTrue(num_eh_primo(13))
        
unittest.main()