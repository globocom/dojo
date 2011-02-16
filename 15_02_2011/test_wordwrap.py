import unittest
from wordwrap import wrap

class WordWrapTest(unittest.TestCase):
    
    def test_quebra_de_linha_no_fim_de_uma_palavra(self):
        self.assertEquals(wrap('word', 5), 'word')
    
    def test_quebra_de_linha_com_duas_palavras_que_excedem_o_tamanho_da_coluna(self):
        self.assertEquals(wrap('two words', 4), 'two\nwords')

    def test_palavra_maior_que_tamanho_da_coluna(self):
        self.assertEquals(wrap('bigword', 4), 'bigword')

    def test_quebra_de_linha_com_duas_palavras_maiores_que_o_tamanho_da_coluna(self):
        self.assertEquals(wrap('bigword bigword', 4), 'bigword\nbigword')

    def test_palavras_menores_que_tamanho_da_coluna(self):
        self.assertEquals(wrap('big word', 15), 'big word')
        
    def test_tres_palavras_com_duas_com_tamanho_menor_que_a_quantidade_de_colunas(self):
        self.assertEquals(wrap('quer misto quente?', 10), 'quer misto\nquente?')
    
    def test_tres_linhas(self):
        self.assertEquals(wrap('loren loren loren', 3), 'loren\nloren\nloren')
        
    def test_tres_linhas_com_espaco_na_primeira_linha(self):
        self.assertEquals(wrap('loren loren loren loren loren loren', 11), 'loren loren\nloren loren\nloren loren')
        
    def test_tres_linhas_com_mais_de_um_espaco_entre_palavras(self):
        self.assertEquals(wrap('loren        loren', 7), 'loren\nloren')
        
    def test_duas_linhas_com_barra_n(self):
        self.assertEquals(wrap('loren\nloren loren', 11), 'loren\nloren loren')
    
    
unittest.main()