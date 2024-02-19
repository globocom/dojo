import unittest
from dojo import quantity_letter, quantity_letters, main


class DojoTest(unittest.TestCase):
    def test_quantity_letter_l(self):
        self.assertEqual(quantity_letter('hello', 'l'), 2)

    def test_quantity_letter_e(self):
        self.assertEqual(quantity_letter('hello', 'e'), 1)

    def test_quantity_letter_r(self):
        self.assertEqual(quantity_letter('hello', 'r'), 0)

    def test_quantity_letters_1(self):
        self.assertDictEqual(quantity_letters('hello'), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
    
    def test_quantity_letters_2(self):
        self.assertDictEqual(quantity_letters('abc'), {'a': 1, 'b': 1, 'c': 1})

    def test_quantity_letters_3(self):
        self.assertDictEqual(quantity_letters('abcc'), {'a': 1, 'b': 1, 'c': 2})

    def test_main(self):
        self.assertDictEqual(main('hello'), {'l': 2, 'e': 1, 'h': 1})

    def test_main2(self):
        self.assertDictEqual(main('abcc'), {'c': 2, 'a': 1, 'b': 1})

    def test_main3(self):
        self.assertDictEqual(main('aabbbccde'), {'b': 3, 'a': 2, 'c': 2})

if __name__ == '__main__':
    unittest.main()
