import unittest
from dojo import main, prepare_input, count_words, filter_bans


class DojoTest(unittest.TestCase):
    def test_prepare_input_1(self):
        self.assertListEqual(
            prepare_input("Bob hit a ball"),
            ["bob", "hit", "a", "ball"]
        )
    def test_prepare_input_2(self):
        self.assertListEqual(
            prepare_input("Alice,. hit a ball."),
            ["alice", "hit", "a", "ball"]
        )
    def test_prepare_input_3(self):
        self.assertListEqual(
            prepare_input("Pedro,.hit a ball."),
            ["pedrohit", "a", "ball"]
        )

    def test_count_words_1(self):
        self.assertDictEqual(
            count_words(["pedrohit", "a", "ball"]),
            {'pedrohit': 1, 'a':1, 'ball':1}
        )
    def test_count_words_2(self):
        self.assertDictEqual(
            count_words(["a", "a", "ball"]),
            {'a':2, 'ball':1}
        )

    def test_count_words_3(self):
        self.assertDictEqual(
            count_words(["b", "a", "ball"]),
            {'b': 1, 'a':1, 'ball':1}
        )


    def test_filter_bans_1(self):
        self.assertDictEqual(
            filter_bans({'b': 1, 'a':1, 'ball':1}, {"b"}),
            {'a':1, 'ball':1}
        )

    def test_filter_bans_2(self):
        self.assertDictEqual(
            filter_bans({'b': 1, 'a':1, 'ball':1}, {"b", "a"}),
            {'ball':1}
        )

    def test_filter_bans_3(self):
        self.assertDictEqual(
            filter_bans({'b': 1, 'a':1, 'ball':1}, {"b", "a", 'ball'}),
            {}
        )

#Bob hit a ball, the hit BALL flew far after it was hit.

if __name__ == '__main__':
    unittest.main()

# Lara - Tiago - João - Sami - Ingrid - Juan
# paragraph = "a.", banned = []
# remover os caracteres
# transformar em lowercase
# separar palavras para uma lista

# function -> tratar a palavra inicial
# function -> contador
# function -> filtro banidos
# function -> mais repetida
