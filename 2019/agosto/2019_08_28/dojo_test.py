import unittest
from dojo import count_vowels, get_score, get_total_score


class DojoTest(unittest.TestCase):

    def test_count_vowels_1(self):
        self.assertEqual(count_vowels('programming'), 3)

    def test_count_vowels_2(self):
        self.assertEqual(count_vowels('hacker'), 2)

    def test_count_vowels_3(self):
        self.assertEqual(count_vowels('is'), 1)

    def test_score_hacker_equals_2(self):
        self.assertEqual(get_score('hacker'), 2)

    def test_score_programming_equals_1(self):
        self.assertEqual(get_score('programming'), 1)
    
    def test_score_is_equals_1(self):
        self.assertEqual(get_score('is'), 1)

    def test_total_score_1(self):
        self.assertEqual(get_total_score('hacker book'), 4)

    def test_total_score_2(self):
        self.assertEqual(get_total_score('programming is awesomee'), 3)

    def test_total_score_3(self):
        self.assertEqual(get_total_score('the book is on the table'), 8)


if __name__ == '__main__':
    unittest.main()
