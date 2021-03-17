import unittest
from dojo import separate_names, get_bigger_name, ordenados

entrada = [['Joao', 'NO'], ['Carlos', 'YES'], ['Abner', 'NO'], ['Samuel', 'YES'], ['Ricardo', 'NO'], ['Abhay', 'YES'], ['Samuel', 'YES'], ['Andres', 'YES']]
class DojoTest(unittest.TestCase):
    def test_separate_names(self):
        self.assertEqual(separate_names(entrada), (["Carlos", "Samuel", "Abhay", "Samuel", "Andres",],["Joao", "Abner", "Ricardo"])) 

    def test_get_bigger_name(self):
        self.assertEqual(get_bigger_name(["Carlos", "Samuel", "Abhay", "Samuel", "Andres"]), "Carlos") 

    def test_ordenados(self):
        self.assertEqual(ordenados(["Carlos", "Samuel", "Abhay", "Samuel", "Andres"]), ["Abhay", "Andres", "Carlos", "Samuel"])
if __name__ == '__main__':
    unittest.main()


# Juan - Ingrid - Lara - Tiago

# [['Joao', 'NO'], ['Carlos', 'YES'], ['Abner', 'NO'], ['Samuel', 'YES'], ['Ricardo', 'NO'], ['Abhay', 'YES'], ['Samuel', 'YES'], ['Andres', 'YES'], ['Roberto', 'NO'], ['Carlos', 'YES'], ['Samuel', 'YES'], ['Samuel', 'YES'], ['Abhay', 'YES'], ['Aline', 'YES'], ['Andres', 'YES']]
# [[]] 
#['Joao','Abner', ] 
# 1 - Processar input -> Colocar numa lista de listas

# 2 - Separar em pessoas que colocaram Yes e não
    # Enquanto estamos colocando as pessoas do Yes na lista:
     # Teremos uma variavel que vai ter o nome com maior quantidade de letras
     # quando for inserir um novo nome na lista do yes, verificar se a quantidade é maior
     # se for, troca a variavel, se não, não troca

# 3 - No final ordena alfabeticamente as listas e faz um concat das que tem sim com não.''''Carlos','Abner''Samuel','Ricardo','Abhay'