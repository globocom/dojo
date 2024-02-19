import unittest
from dojo import get_position, main


class DojoTest(unittest.TestCase):
    def test_get_position_1(self):
        self.assertEquals(get_position(0, 2, 3), 6)

    def test_get_position_2(self):
        self.assertEquals(get_position(1, 1, 1), 2)

    def test_get_position_3(self):
        self.assertEquals(get_position(3, 2, 1), 5)

    def test_get_result1(self):
        self.assertEquals(main(1, 2, 8, 1), True)
    
    def test_get_result2(self):
        self.assertEquals(main(1, 3, 8, 1), False)

    def test_get_result3(self):
        self.assertEquals(main(0, 2, 8, 1), True )

# x2 - x1 / t1 - t2
if __name__ == '__main__':
    unittest.main()

# get_position(initial_position, distance, qnt_saltos)

# Xaulim100 / Allan
# DarkAngel666 / Mateus
# Elen / Elen
# Don Juan / Juan
# Naty / Natalia
# Steve Universe / Tiago
# Samuel / Sami 