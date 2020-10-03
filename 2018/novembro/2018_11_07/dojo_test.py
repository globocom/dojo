import unittest
from dojo import main


class DojoTest(unittest.TestCase):
    def test_tamanho_palavra(self):
        self.assertEqual(main("a"), "a")

    def test_tamanho_palavra_2(self):
        self.assertEqual(main("aa"), "aa")

    def test_tamanho_palavra_3(self):
        self.assertEqual(main("aaa"), "aaa")

    def test_tamanho_palavra_4(self):
        self.assertEqual(main("bbb"), "bbb")

    def test_tamanho_palavra_5(self):
        self.assertEqual(main("aaabb"), "aaa")

    def test_tamanho_palavra_6(self):
        self.assertEqual(main("bbbaa"), "bbb")

    def test_tamanho_palavra_7(self):
        self.assertEqual(main("aabbbb"), "bbbb")

    def test_tamanho_palavra_8(self):
        self.assertEqual(main("aabbbbaaa"), "bbbb")


if __name__ == '__main__':
    unittest.main()
