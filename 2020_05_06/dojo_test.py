import unittest
from dojo import remove_white_spaces, get_square_root_of_length, get_matrix


class DojoTest(unittest.TestCase):
    def test_remove_white_space_1(self):
        self.assertEqual(remove_white_spaces(
            'have a nice day'), "haveaniceday")

    def test_remove_white_space_2(self):
        self.assertEqual(remove_white_spaces(
            'have a good day'), "haveagoodday")

    def test_remove_white_space_3(self):
        self.assertEqual(remove_white_spaces(
            'have a wonderful day'), "haveawonderfulday")

    def test_get_square_root_of_sentence_1(self):
        self.assertEqual(get_square_root_of_length(
            'haveawonderfulday'), [4, 5])

    def test_get_square_root_of_sentence_2(self):
        self.assertEqual(get_square_root_of_length('haveagoodday'), [3, 4])

    def test_get_square_root_of_sentence_3(self):
        self.assertEqual(get_square_root_of_length(
            'havewonderfulnicegoodokayday'), [5, 6])

    def test_get_matrix_1(self):
        self.assertEqual(get_matrix('havewonderfulnicegoodokayday', [5, 6]),
                         ['havewo', 'nderfu', 'lniceg', 'oodoka', 'yday'])

    def test_get_matrix_2(self):
        self.assertEqual(get_matrix('haveawonderfulday', [4, 5]),
                         ['havea', 'wonde', 'rfuld', 'ay'])

    def test_get_matrix_3(self):
        self.assertEqual(get_matrix('aaabbbcccbbb', [3, 4]), [
                         'aaab', 'bbcc', 'cbbb'])


if __name__ == '__main__':
    unittest.main()

# Ingrid - Icaro - Sami - Juan
