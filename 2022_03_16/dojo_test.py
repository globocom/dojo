import unittest
from dojo import *


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertEqual(main(), 236)

    def test_contains_vowels_should_return_false_if_string_contains_at_least_one_vowel(
        self,
    ):
        contains = contains_vowels("a")
        self.assertFalse(contains)

    def test_contains_vowels_should_return_false_if_string_contains_at_least_two_vowel(
        self,
    ):
        contains = contains_vowels("aebc")
        self.assertFalse(contains)

    def test_contains_vowels_should_return_true_if_string_contains_at_least_four_vowel(
        self,
    ):
        contains = contains_vowels("eioa")
        self.assertTrue(contains)

    def test_contains_vowels_should_return_true_if_string_contains_at_least_four_vowel_2(
        self,
    ):
        contains = contains_vowels("eiobcbc")
        self.assertTrue(contains)

    def test_contains_double_letter_false_if_one_letter_str(self):
        self.assertFalse(contains_double_letter("a"))

    def test_contains_double_letter_two_if_two_letter_str(self):
        self.assertTrue(contains_double_letter("aa"))

    def test_contains_double_letter_two_if_three_letter_str(self):
        self.assertTrue(contains_double_letter("bbb"))

    def test_contains_double_letter_two_if_three_letter_str_dif(self):
        self.assertFalse(contains_double_letter("avc"))

    def test_not_contains_forbidden_should_return_false_if_no_forbidden_string_is_find(
        self,
    ):
        self.assertFalse(contains_forbidden("aa"))

    def test_not_contains_forbidden_should_return_true_if_1_forbidden_string_is_find(
        self,
    ):
        self.assertTrue(contains_forbidden("ab"))

    def test_not_contains_forbidden_should_return_true_if_2_forbidden_string_is_find(
        self,
    ):
        self.assertTrue(contains_forbidden("xxxxxxab"))

    def test_not_contains_forbidden_should_return_true_if_3_forbidden_string_is_find(
        self,
    ):
        self.assertTrue(contains_forbidden("xxcdxxx"))

    def test_validate_nice_string_1(self):
        self.assertTrue(validate_nice_string("ugknbfddgicrmopn"))

    def test_validate_nice_string_2(self):
        self.assertFalse(validate_nice_string("jchzalrnumimnmhp"))


if __name__ == "__main__":
    unittest.main()


# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
