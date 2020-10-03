import unittest
from dojo import swap_numbers, index_less_element, sort_array


class DojoTest(unittest.TestCase):
    def test_swap_numbers(self):
        arr = [2,1]
        self.assertEqual(swap_numbers(0,1,arr), [1,2])

    def test_swap_numbers2(self):
        arr = [4,1]
        self.assertEqual(swap_numbers(0,1,arr), [1,4])

    def test_swap_numbers3(self):
        arr = [6,1,8]
        self.assertEqual(swap_numbers(0,1,arr), [1,6,8])

    def test_invalid_negative_pos(self): 
        arr = [6,1,8,4]
        self.assertEqual(swap_numbers(-1,3, arr), arr)
    
    def test_invalid_larger_pos(self): 
        arr = [6,1,8,4]
        self.assertEqual(swap_numbers(2,4, arr), arr)
    
    def test_get_index_of_less_element(self):
        arr = [6,1,8,3]
        self.assertEqual(index_less_element(arr), 1)

        arr = [6,5,8,4]
        self.assertEqual(index_less_element(arr), 3)
    
    def test_sort_array(self):
        arr = [6,5,8,4]
        self.assertEqual(sort_array(arr), 2)

    def test_sort_array2(self):
        arr = [6,3,8,4]
        self.assertEqual(sort_array(arr), 3)

    def test_sort_array3(self):
        arr = [2,3,1,4]
        self.assertEqual(sort_array(arr), 2)

if __name__ == '__main__':
    unittest.main()
