import unittest
from dojo import *


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(main())
    
    def test_listExists(self):
        self.assertTrue(inputLength([1,2,3]))

    def test_listExists2(self):
        self.assertTrue(inputLength([-1,5,7]))

    def test_listExists3(self):
        self.assertTrue(inputLength([-3,7,0]))

    def test_listExists4(self):
        self.assertFalse(inputLength([]))

    def test_Countdown1(self):
        self.assertEqual(countDown([9,4,3,2,1], 4), 1)
        
    def test_Countdown2(self):
        self.assertEqual(countDown([9,1,2,2,1,2,1], 2), 2)

    def test_Countdown3(self):
        self.assertEqual(countDown([9,4,3,2,0,1], 4), 0)

    def test_Countdown5(self):
        self.assertEqual(countDown([9,4,3,2,0,1], 8), 0)


if __name__ == '__main__':
    unittest.main()


# [9,4,3,2,1], 4 -> 1
# [9,1,2,2,1,2,1], 2 ->  2
# [9,4,3,2,0,1], 4 -> 0


# condições iniciais
# - se o arr tem len 0 -> return 0

# ? primeiro procurar o número 1
# ? primeiro procurar o número K
# ? verificar entre o indice do K e o indice mais K 

# [9,4,3,2,1], -----> Cuidado acessar indice fora do range do vetor
#    ^ --- ^