import unittest
from dojo import main


class DojoTest(unittest.TestCase):
    def test_array_length_1(self):
        self.assertEquals(main([1], 1), [[1]])

    def test_array_length_2(self):
        self.assertEquals(main([2, 3], 2), [[2]])

    def test_array_length_2_1(self):
        self.assertEquals(main([2, 3], 5), [[2, 3]])

    def test_array_length_2_3(self):
        self.assertEquals(main([2, 3], 4), [[2, 2]])



if __name__ == '__main__':
    unittest.main()
