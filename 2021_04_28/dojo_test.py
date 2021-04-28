import unittest
from dojo import criar_fita, main, pinta_fita


class DojoTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(4, [1]), 3)

    def test_main_outro(self):
        self.assertEqual(main(13, [2, 3, 6]), 3)

    def test_main_outro(self):
        self.assertEqual(main(10, [9, 10]), 8)

    def test_criar_fita(self):
        fita = [1, 0, 0, 0]
        self.assertListEqual(criar_fita(4, [1]), fita)
    
    def test_criar_fita_vazia(self):
        self.assertListEqual(criar_fita(0, []), [])

    def test_criar_fita_3(self):
        fita = [1,1,0]
        self.assertListEqual(criar_fita(3, [1,2]), fita)

    def test_criar_fita_3(self):
        fita = [1,1,0]
        self.assertListEqual(criar_fita(3, [1,2]), fita)

    def test_pinta_fita(self):
        fita = [1,1,0]
        fita_pintada = [1,1,1]
        self.assertListEqual(pinta_fita(fita), fita_pintada)

    def test_pinta_fita2(self):
        fita = [1, 0, 0, 0]
        fita_pintada = [1, 1, 0, 0]
        self.assertListEqual(pinta_fita(fita), fita_pintada)
        
    def test_pinta_fita2(self):
        fita = [0, 1, 0]
        fita_pintada = [1, 1, 1]
        self.assertListEqual(pinta_fita(fita), fita_pintada)

# [0,1,0,0,0,1,0,0,0,0,0,1]
if __name__ == '__main__':
    unittest.main()

#Joao - Ingrid - Lara - Juan - Tiago

# n = tamanho da fita => [0,0,1,0,1]
# x,y,x = as posições dos pingos
# espera a quantidade de dias que vai demorar pra ela estar completamente preta

# transforma input em array

#funcao que pinta
    # while existe algum elemento = 0 no array
        # vamos pintando o antes e depois de todos os uns

# 13 3 
# 2 6 13

# 10 2 
# 9 10 