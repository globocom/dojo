import unittest
from dojo import result, main


class DojoTest(unittest.TestCase):
    def test_10dolares(self):
        self.assertEquals(result(10, 10),(0,1))
    

    def test_90dolares(self):
        self.assertEquals(result(90, 50),(40,1))
    

    def test_65dolares(self):
        self.assertEquals(result(65, 20),(5,3))
    
    def test_main10(self):
        self.assertEquals(main(10),[(10,1)])

    def test_main30(self):
        self.assertEquals(main(30),[(20,1),(10,1)])

    def test_main40(self):
        self.assertEquals(main(40),[(20,2)])

if __name__ == '__main__':
    unittest.main()





# informa valor (60) e nota atual (50)
# func retorna (1, 10)


# int : valor de saque
# [(valor_da_nota, qnt_da_nota),(valor_da_nota, qnt_da_nota)]

## sacar 60 reais
## [(50,1),(10,1)]

# 60 % 50 = 10
# 60 // 50 = 1

# 10 // 20 = 0
# 10 % 20 = 10

# 10 // 10 = 1
# 10 % 10 = 0

#Elen
#----------------
#60 >= 100? n
#60 >= 50? y

#60 - 50 = 10
#cont 1 _ 50

#10 >=100? n
#10 >= 50? n
#10 >= 20? n
#10 >= 10? y

#10 - 10 = 0
#cont 1 _ 10
#---------------


# juan
# elen
# mateus
# allan
# ingrid


