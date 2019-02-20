import unittest
from dojo import in_array, array_list


class DojoTest(unittest.TestCase):
    def test_check_array(self):
        self.assertTrue(in_array([1, 2, 3], 1))


    def test_check_array5(self):
        self.assertFalse(in_array([1, 2, 3], 5))

    def test_check_array_has_4(self):
        self.assertTrue(in_array([1, 2, 4], 4))

    def test_check_array_list(self):
        self.assertEquals(array_list([[1, 2, 3], [2, 5, 6]]), [2])

    def test_check_array_list2(self):
        self.assertEquals(array_list([[1, 2, 3], [4, 5, 6]]), [])

    def test_check_array_list3(self):
        self.assertEquals(array_list([[1, 2, 3], [3, 5, 6]]), [3])

    def test_check_array_list4(self):
        self.assertEquals(array_list([[1, 2, 3], [1, 3, 6], [1, 4, 7]]), [1])

    def test_check_array_list5(self):
        self.assertEquals(array_list([[0, 2, 3], [1, 3, 6], [1, 4, 7]]), [])

    def test_check_array_list5(self):
        self.assertEquals(array_list([[0, 2, 7], [1, 3, 7], [1, 4, 7]]), [7])
if __name__ == '__main__':
    unittest.main()
