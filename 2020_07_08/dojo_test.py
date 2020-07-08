import unittest
from dojo import string_to_array, main


class DojoTest(unittest.TestCase):
    def test_two_letters(self):
        self.assertEqual(string_to_array('ab'),['a','b'])

    def test_one_letters(self):
        self.assertEqual(string_to_array('a'),['a'])
        
    def test_four_letters(self):
        self.assertEqual(string_to_array('abcd'),['a', 'b', 'c', 'd'])
    
    def test_main_four_stones(self):
        self.assertEqual(main('abcd','abcdY'),4)

    def test_main_five_stones(self):
        self.assertEqual(main('abcd','abcYS'),3)

    def test_main_seven_stones(self):
        self.assertEqual(main('abcde','abcdeYS'),5)

    def test_main_eight_stones(self):
        self.assertEqual(main('aA','aAAbbbbb'),3)

if __name__ == '__main__':
    unittest.main()

# Juan - Allan - Sami - Icaro - Ingrid - Mateus(top) - Elen
