import unittest
from dojo import *


class DojoTest(unittest.TestCase):
    def test_equal_arrays_1(self):
        self.assertEqual(main([1, 2], [1]), [2])

    def test_equal_arrays_2(self):
        self.assertEqual(main([1, 2, 3], [1]), [2, 3])

    def test_getcount_with_numbers_1(self):
        self.assertEqual(getcount([1]), {1: 1})

    def test_getcount_with_numbers_2(self):
        self.assertEqual(getcount([1, 1]), {1: 2})

    def test_dictdiff(self):
        self.assertEqual(dictdiff({1: 1}, {1: 2}), [1])

    def test_dictdiff_2(self):
        self.assertEqual(dictdiff({1: 2, 2: 1}, {1: 1}), [1, 2])

    def test_dictdiff_3(self):
        self.assertEqual(dictdiff({1: 1}, {1: 2, 2: 1}), [1, 2])


if __name__ == '__main__':
    unittest.main()
