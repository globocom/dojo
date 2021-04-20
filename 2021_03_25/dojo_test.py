import unittest
from dojo import main, calc_golpe, ganhador


class DojoTest(unittest.TestCase):
    def test_calc_golpe(self):
        self.assertEquals(calc_golpe(5, (12, 23, 15)), 17.5)
    def test_calc_golpe_false(self):
        self.assertEquals(calc_golpe(5, (42, 12, 21)), 27)
    def test_calc_golpe_bonus(self):
        self.assertEquals(calc_golpe(5, (42, 12, 20)), 32)
    def test_ganhador(self):
        self.assertEquals(ganhador(5, (12, 23, 15), (42, 12, 21)), "guarte")
    def test_ganhador(self):

if __name__ == '__main__':
    unittest.main()

"""
Participantes (ordem):

Jose victor Medeiros
Alice
"""