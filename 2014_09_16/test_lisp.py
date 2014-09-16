#coding: utf-8

import unittest

from lisp import T8l


class T8lTestCase(unittest.TestCase):

    def test_creates_a_t8l_with_words(self):
        words = ["good", "bad", "ugly"]
        t8l = T8l(words)
        self.assertEqual(t8l.words, words)
        translations = ["9883", "753", "7983"]
        self.assertEqual(t8l.translated_words, translations)

    def test_translate_word_a_to_numbers(self):
        word = 'a'
        t8l = T8l([])
        returned = t8l.to_numbers(word)
        expected = '5'
        self.assertEqual(returned, expected)

    def test_translate_word_bola_to_numbers(self):
        word = 'bola'
        t8l = T8l([])
        returned = t8l.to_numbers(word)
        expected = '7885'
        self.assertEqual(returned, expected)

    def test_translate_numbers_to_words(self):
        t8l = T8l(['good'])
        self.assertEqual(t8l.to_words('9883'), ['good'])

    def test_translate_numbers_to_two_words(self):
        t8l = T8l(['good', 'ugly'])
        self.assertEqual(t8l.to_words('98837983'), ['good', 'ugly'])

    def test_translate_numbers_to_two_words(self):
        t8l = T8l(['go', 'good', 'od'])
        self.assertEqual(t8l.to_words('98837983'), ['good', 'ugly'])



if __name__ == "__main__":
	unittest.main()
