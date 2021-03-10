import unittest
from dojo import level_is_even, value_coup, main


class DojoTest(unittest.TestCase):
  def test_level_is_even_1(self):
    self.assertTrue(level_is_even(2))

  def test_level_is_even_2(self):
    self.assertFalse(level_is_even(1))

  def test_level_is_even_3(self):
    self.assertFalse(level_is_even(3))
  
  def test_value_coup_1(self):
    self.assertEqual(value_coup(12,23,15, 5), 17.5)

  def test_value_coup_2(self):
    self.assertEqual(value_coup(42,12,20, 5), 32)

  def test_value_coup_3(self):
    self.assertEqual(value_coup(52,1,11, 2), 26.5)

  def test_main(self):
    self.assertEqual(main(5,[12,23,15],[42,12,20]), "Duarte")

  def test_main2(self):
    self.assertEqual(main(2,[52,1,11],[1,52,1]), "Empate")

  def test_main3(self):
    self.assertEqual(main(3,[95,12,22],[5,51,21]), "Gabriel")


if __name__ == '__main__':
  unittest.main()

#Bonus
#ataque, defesa, level
#(ataque + defesa) /2 + bonus (se level for par)

# 3
# 5
# 12 23 15
# 42 12 20
# 2
# 52 1 11
# 1 52 1
# 3
# 95 12 22
# 5 51 21