import unittest
from dojo import main, walk_matrix

class DojoTest(unittest.TestCase):
    def test_true(self): self.assertTrue(main())

    def test1_walk_matrix(self):
        matrix = [[1,2,3],[8,9,4],[7,6,5]]
        direction = "RIGHT"
        border = (0,0,2,2)
        self.assertEqual(walk_matrix( matrix, direction, border), [ (0,0), (0,1), (0,2) ])

    def test2_walk_matrix(self):
        matrix = [[1,2,3],[8,9,4],[7,6,5]]
        direction = "DOWN"
        border = (0,1,2,2)
        self.assertEqual(walk_matrix( matrix, direction, border), [ (1,2), (2,2) ])

    def test3_walk_matrix(self):
        matrix = [[1,2,3],[8,9,4],[7,6,5]]
        direction = "LEFT"
        border = (0,1,1,2)
        self.assertEqual(walk_matrix( matrix, direction, border), [ (2,1), (2,0) ])

    def test4_walk_matrix(self):
        matrix = [[1,2,3],[8,9,4],[7,6,5]]
        direction = "UP"
        border = (0,1,1,1)
        self.assertEqual(walk_matrix( matrix, direction, border), [ (1,0) ])

            
if __name__ == '__main__':
    unittest.main()

# Ordem: Tiago - Juan - Ighor - Lara - Henrique - Ingrid - Elen


# Algoritmo:
# left = 0; top = 0; right = 2; bottom = 2
#   1. percorrer primeira linha
#   2. percorrer última coluna
#   3. percorrer ultima linha (inverso)
#   4. percorrer primeira linha (inverso)
# 

# Exemplos
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

# Direita => incrementar o top 
# Baixo => decrementar o right
# Esquerda => decrementar o bottom
# Cima => incrementa o left

#                        #     left = 0; top = 0; right = 2; bottom = 2
# [0][0], [0][1], [0][2] # R-> left = 0; top = 1; right = 2; bottom = 2
# [1][2], [2][2]         # B-> left = 0; top = 1; right = 1; bottom = 2
# [2][1], [2][0]         # <-L left = 0; top = 1; right = 1; bottom = 1
# [1][0]                 # <-T left = 1; top = 1; right = 1; bottom = 1
# [1][1]                 # R->         ; top = 2

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]# snail(array) #=> [1,2,3,6,9,8,7,4,5]