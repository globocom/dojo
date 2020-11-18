import unittest
from dojo import split_shoe, check_shoe


class DojoTest(unittest.TestCase):
    def test_split_shoe1(self):
        self.assertEqual(split_shoe("40 D"), [40,"D"])
    def test_split_shoe2(self):
        self.assertEqual(split_shoe("41 E"), [41,"E"])
    def test_split_shoe3(self):
        self.assertEqual(split_shoe("41 D"), [41,"D"])

    def test_check_shoe1(self):
        self.assertEqual(check_shoe(["40 D", "41 E", "41 D", "40 E"]), 2)
    def test_check_shoe2(self):
        self.assertEqual(check_shoe(["38 E", "38 E", "40 D", "38 D", "40 D", "37 E"]), 1)
    def test_check_shoe3(self):
        self.assertEqual(check_shoe(["38 E"]), 0)
        

if __name__ == '__main__':
    unittest.main()

#Ordem: Ingrid -  Lara - Tiago Figueiredo - Tiago Carreira -Lucas - Sami - Miguel
if __name__ == '__main__':
    unittest.main()

#Ordem: Ingrid -  Lara - Tiago Figueiredo - Tiago Carreira -Lucas - Sami - Miguel
'''

Exemplo de Entrada	Exemplo de Saída
4
40 D
41 E
41 D
40 E

[RESPOSTA] 2

6
38 E
38 E
40 D
38 D
40 D
37 E

[RESPOSTA] 1
'''