import unittest
from dojo import main, to_lower, remove_pontuation, reverse_string, is_palindrome


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(main())

    def test_to_lower_1(self):
        self.assertEqual(to_lower("AbC"), "abc")
    def test_to_lower_2(self):
        self.assertEqual(to_lower("de1"), "de1")
    def test_to_lower_3(self):
        self.assertEqual(to_lower("TEXT"), "text")

    def test_remove_pontuation_1(self):
        self.assertEqual(remove_pontuation('oi, oi'), 'oioi')
    def test_remove_pontuation_2(self):
        self.assertEqual(remove_pontuation('!oi, $io'), 'oiio')
    def test_remove_pontuation_3(self):
        self.assertEqual(remove_pontuation('#$%!@#$'), '')

    def test_reverse_string_1(self):
        self.assertEqual(reverse_string('comovai'), 'iavomoc')
    def test_reverse_string_2(self):
        self.assertEqual(reverse_string('a'), 'a')
    def test_reverse_string_3(self):
        self.assertEqual(reverse_string('abc0'), '0cba')

    def test_is_palindrome_1(self):
        self.assertTrue(is_palindrome('ana'))
    def test_is_palindrome_2(self):
        self.assertFalse(is_palindrome('ane'))
    def test_is_palindrome_3(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
    def test_is_palindrome_4(self):
        self.assertFalse(is_palindrome("race a car"))

if __name__ == '__main__':
    unittest.main()




# Algoritmo #1:

# 1. trasnformar input
#   1. passar tudo para lower case
#   2. remover pontuação
# 2. inverter string
# 3. comparar input com o reversed


# input   = abcdefedcba
# reverse = abcdefedcba


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
