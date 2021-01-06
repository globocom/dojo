import unittest
from dojo import get_dimensions, build_matrix


class DojoTest(unittest.TestCase):
    def test_get_dimensions1(self):
        self.assertEquals(get_dimensions("ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"), (7,8))
    def test_get_dimensions2(self):
        self.assertEquals(get_dimensions("feedthedog"), (3,4))
    def test_get_dimensions2(self):
        self.assertEquals(get_dimensions("chillout"), (3,3))
    def test_build_matrix(self):
        self.assertEquals(build_matrix("if man was me ant to stay on the ground god would have given us roots"), 
        [
            ['i','f','m','a','n','w','a','s'],
            ['m','e','a','n','t','t','o','s'],
            ['t','a','y','o','n','t','h','e'],
            ['g','r','o','u','n','d','g','o'],
            ['d','w','o','u','l','d','h','a'],
            ['v','e','g','i','v','e','n','u'],
            ['s','r','o','o','t','s','','']
        ])
    
    def test_build_matrix2(self):
        self.assertEqual(build_matrix("feed the dog"), 
        [
            ['f','e','e','d'],
            ['t','h','e','d'],
            ['o','g','',''],
        ])

    def test_build_matrix3(self):
        self.assertEqual(build_matrix("chill out"), 
        [
            ['c','h','i'],
            ['l','l','o'],
            ['u','t','']
        ]) 

if __name__ == '__main__':
    unittest.main()


# Allan - Carreira - Elen  - Lucas - Bruna - Lara - Mateus - TiagoDuarte - Ighor
'''
  

  
'm','e','a','n','t','t','o','s'          
't','a','y','o','n','t','h','e'  
'g','r','o','u','n','d','g','o'  
'd','w','o','u','l','d','h','a'  
'v','e','g','i','v','e','n','u'  
's','r','o','o','t','s'
','


feed the dog    

[
['f','e','e','d'],
['t','h','e','d'],
['o','g','',''],
]

['c','h','i']
['l','l','o']
['u','t',']
'
'


def bla(str):
    
'''
# EU JÁ TE SUPEREEEEI, EU JÁ TE SUPEREEEEEEEEEEI 

# mas nao manda mensagem outra vez SE NAO RECAIREEEI (HINO!) #amo


# 1 - Tirar os espaçoes da string 
# 2 - Dimensões da matriz com base na string (sem espaços) - FEITO
# 3 - Construir a matriz
# 4 - Montar a string
