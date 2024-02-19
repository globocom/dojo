import unittest
from dojo import main


class DojoTest(unittest.TestCase):
    def test_foo(self):
        self.assertEqual([["a",None,None],
                          [None,"b",None],
                          [None,None,"c"]], main("abc"))


    def test_foo2(self):
        self.assertEqual([["a",None,None],
                          [None,"b",None],
                          [None,None,"d"]], main("abd"))


    def test_foo3(self):
        self.assertEqual([["a",None,None],
                          [None,"e",None],
                          [None,None,"w"]], main("aew"))

    def test_foo4(self):
        self.assertEqual([["a",None,None, None],
                          [None,"b",None, "d"],
                          [None,None,"c", None]], main("abcd"))

    def test_foo4(self):
        self.assertEqual([["a",None,None, None, "e"],
                          [None,"b",None, "d", None],
                          [None,None,"c", None, None]], main("abcde"))

    def test_foo5(self):
        self.assertEqual([["W",None,None, None, "E",None,None, None],
                          [None,"E",None, "R", None,None,None, None],
                          [None,None,"A", None,None,None, None, None]], main("WEAREDISCOVEREDFLEEATONCE"))

if __name__ == '__main__':
    unittest.main()