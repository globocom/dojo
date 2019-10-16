import unittest
from dojo import BuildStr


class DojoTest(unittest.TestCase):
    def test_append_a(self):
        mystr = BuildStr(1, 2, 3)
        mystr.append('a')
        self.assertEqual(mystr.string, 'a')

    def test_append_b(self):
        mystr = BuildStr(1, 2, 3)
        mystr.append('b')
        self.assertEqual(mystr.string, 'b')

    def test_append_ba(self):
        mystr = BuildStr(1, 2, 3)
        mystr.append('b')
        mystr.append('a')
        self.assertEqual(mystr.string, 'ba')

    def test_find(self):
        mystr = BuildStr(1, 2, 3)
        mystr.string = 'bannc'
        self.assertTrue(mystr.find('ba'))

    def test_find_2(self):
        mystr = BuildStr(1, 2, 3)
        mystr.string = 'bannc'
        self.assertFalse(mystr.find('ab'))

    def test_find_3(self):
        mystr = BuildStr(1, 2, 3)
        mystr.string = 'bannc'
        self.assertTrue(mystr.find('bann'))

    def test_pop_chars(self):
        mystr = BuildStr('abcdef', 2, 3)
        self.assertEqual('def', mystr.pop_chars(3))

    def test_pop_chars_2(self):
        mystr = BuildStr('abcdef', 2, 3)
        self.assertEqual('ef', mystr.pop_chars(4))


if __name__ == '__main__':
    unittest.main()
