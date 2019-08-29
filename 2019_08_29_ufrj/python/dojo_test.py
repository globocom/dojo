import unittest
from dojo import getProtocol
from dojo import getDomain
from dojo import getSubD
from dojo import parserUrl


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertEqual(getProtocol("http://globo.com"), "http")

    def test_true2(self):
        self.assertEqual(getProtocol("https://globo.com"), "https")

    def test_true3(self):
        self.assertEqual(getProtocol("ftp://globo.com"), "ftp")

    def test_true4(self):
        self.assertEqual(getDomain("http://globo.com"), "globo.com")

    def test_true5(self):
        self.assertEqual(getDomain("http://globo.com/algumacoisa"), "globo.com")

    def test_true6(self):
        self.assertEqual(getDomain("http://globo.com.br/algumacoisa"), "globo.com.br")

    def test_true7(self):
        self.assertEqual(getSubD("http://g1.globo.com/algumacoisa"), "g1")

    def test_true8(self):
        self.assertEqual(getSubD("http://globo.com/algumacoisa"), None)

    def test_true9(self):
        self.assertEqual(getSubD("http://globo.com.br/algumacoisa"), None)

    def test_true10(self):
        self.assertEqual(getSubD("http://g1.globo.com.br/algumacoisa"), "g1")

    def test_true11(self):
        self.assertEqual(getDomain("https://g1.globo.com/e"), "globo.com")

    def test_true12(self):
        self.assertEqual(parserUrl("https://g1.globo.com/etc")["protocol"], "https")

    def test_true13(self):
        self.assertEqual(parserUrl("https://g1.globo.com/etc")["domain"], "globo.com")


if __name__ == "__main__":
    unittest.main()
