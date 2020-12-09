import unittest
from dojo import main, get_ratio, get_ratio_list, order_desc_by_ratio


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(main())

    def teste_razao1(self) :
        self.assertEquals(get_ratio((2,2)), 1)
    
    def test_razao2(self) :
        self.assertEquals(get_ratio((4,2)), 2)

    def test_razao3(self) :
        self.assertEquals(get_ratio((6,2)), 3)

    def test_get_ratio_list1(self):
        self.assertEquals(get_ratio_list([(15,5), (24,4)]), [(3,15,5), (6,24,4)])

    def test_get_ratio_list2(self):
        self.assertEquals(get_ratio_list([(5,5), (4,4)]), [(1,5,5), (1,4,4)])

    def test_get_ratio_list3(self):
        self.assertEquals(get_ratio_list([(7,5), (9,4)]), [(7/5,7,5), (9/4,9,4)])

    def test_order_desc_by_ratio1(self):
        self.assertEquals(order_desc_by_ratio([(3,15,5), (6,24,4)]), [(6,24,4), (3,15,5)])

    def test_order_desc_by_ratio2(self):
        self.assertEquals(order_desc_by_ratio([(1,5,5), (1,4,4)]), [(1,4,4), (1,5,5)])

    def test_order_desc_by_ratio3(self):
        self.assertEquals(order_desc_by_ratio([(5,5,5), (2,4,4)]), [(5,5,5), (2,4,4)])


if __name__ == '__main__':
    unittest.main()


# Lucas - Tiago - Lara - Carreira

'''
 Funcoes

(X) Pegar as razoes
(x) Contruir a estrutura (razao - tempo - quantidade)
(-) Ordenar pela razao, decrescente
(-) Encontrar a solucao 


- Fazer a razao entre tempo_entrega/numero_pizzas x
- Ordenar os objetos pela razao descrescente
- Pegar os items ate que a soma dos pesos seja 
  menor ou igual ao desejado.
    - Se o peso do item somado ao que ja pegamos for
      maior do que o que desejamos, ignorar o item.

'''