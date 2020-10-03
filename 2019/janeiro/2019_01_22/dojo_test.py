import unittest
from dojo import letter, letter_position, words


class DojoTest(unittest.TestCase):
    def test_letter_a(self):
        self.assertEqual(letter('A'), '2')

    def test_letter_b(self):
        self.assertEqual(letter('B'), '22')

    def test_letter_d(self):
        self.assertEqual(letter('D'), '3')

    def test_letter_g(self):
        self.assertEqual(letter('G'), '4')

    def test_letter_position(self):
        self.assertEqual(letter_position('ABC', 'B'), 2)

    def test_letter_position_zero(self):
        self.assertEqual(letter_position('ABC', 'D'), 0)

    def test_words(self):
        self.assertEqual(words('DOJO'), '36665666')

    def test_words_with_spaces(self):
        self.assertEqual(words('DOJO LEGAL'), '3666566605553342555')

    def test_words_with_repetition(self):
        self.assertEqual(words('DOOJO'), '3666_6665666')

    def test_ab(self):
        self.assertEqual(words('AB'), '2_22')

    def test_words_with_spaces_and_repetition(self):
        self.assertEqual(words('DOOJO LEGAL'), '3666_666566605553342555')


if __name__ == '__main__':
    unittest.main()
