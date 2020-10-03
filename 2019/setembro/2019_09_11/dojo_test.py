import unittest
from dojo import min_array_slices
from dojo import min_iterate
from dojo import array_shuffle

class DojoTest(unittest.TestCase):
    def test_1_and_2(self):
        arr = [1,2]
        self.assertEqual(min_array_slices(arr, 1), [1,2])

    def test__and_2(self):
        arr = [4,5,6]
        self.assertEqual(min_array_slices(arr, 1), [4,11])

    def test__and_2(self):
        arr = [4,5,6,7]
        self.assertEqual(min_array_slices(arr, 2), [9,13])

    def test_min_iterate_3(self):
        arr = [4,5,6]
        self.assertEqual(min_iterate(arr), 3)

    def test_min_iterate_1(self):
        arr = [4,5]
        self.assertEqual(min_iterate(arr), 1)

    def test_min_iterate_3_2(self):
        arr = [4,5,6]
        self.assertEqual(min_iterate(arr), 3)

    def test_min_iterate_2(self):
        arr = [1,2,3,4]
        self.assertEqual(min_iterate(arr), 2)

    def test_array_shuffle(self):
        arr = [1,2]
        self.assertEqual(array_shuffle(arr), [2,1])

    def test_array_shuffle_2(self):
        arr = [1,2,3]
        self.assertEqual(array_shuffle(arr), [1,2,3])
    
    def test_array_shuffle_3(self):
        arr = [1,2,3,4]
        self.assertEqual(array_shuffle(arr), [1,4,2,3])
     

if __name__ == '__main__':
    unittest.main()
