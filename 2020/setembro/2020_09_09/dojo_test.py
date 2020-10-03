import unittest
from dojo import check_sort, remove_element


class DojoTest(unittest.TestCase):
    def test_array_is_not_sorted(self):
        self.assertFalse(check_sort([1,2,3,10,4,2,3,5]))

    def test_array_is_sorted(self):
        self.assertTrue(check_sort([1,2,3,4,5]))

    def test_array_is_sorted(self):
        self.assertFalse(check_sort([2,2,4,6,5]))
    
    def test_array_remove_element(self):
        self.assertEqual(remove_element([2,2,6,3,5],1,2),[2,3,5])

    def test_array_remove_element(self):
        self.assertEqual(remove_element([2,2,6,3,5],0,1),[2,6,3,5])

    def test_array_remove_element(self):
        self.assertEqual(remove_element([2,2,6,3,5],0,2),[6,3,5])
if __name__ == '__main__':
    unittest.main()

# Ingrid / Elen / Sami / Juan / Allan

# [1,2,3,10,4,2,3,5] => [10,4,2] || [3,10,4]
# [1,2,3,5,4,2,6] => [4,2]
# [5,4,3,2,1] => [5,4,3,2] || [4,3,2,1]

# Verificar ordenação -> Remoção -> Passagem pelo array inteiro com cada opção