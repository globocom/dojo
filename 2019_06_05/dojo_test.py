import unittest
from dojo import is_http, is_https, Url

class DojoTest(unittest.TestCase):
    def test_http(self):
        self.assertTrue(is_http("http://g1.globo.com"))

    def test_http_2(self):
        self.assertFalse(is_http("https://g1.globo.com"))

    def test_https(self):
        self.assertTrue(is_https("https://g1.globo.com"))

    def test_https_2(self):
        self.assertFalse(is_https("http://g1.globo.com"))

    def test_url_protocol(self):
        url = Url("http://g1.globo.com")
        self.assertEqual(url.protocol, "http")

    def test_url_domain(self):
        url = Url("https://g1.globo.com")
        self.assertEqual(url.domain, "g1.globo.com")

    def test_url_domain_2(self):
        url = Url("https://:@g1.globo.com")
        self.assertEqual(url.domain, "g1.globo.com")

    def test_url_domain_3(self):
        url = Url("https://user:pass@g1.globo.com")
        self.assertEqual(url.domain, "g1.globo.com")

    def test_url_domain_4(self):
        url = Url("https://user:pass.banana@g1.globo.com")
        self.assertEqual(url.domain, "g1.globo.com")

    def test_url_domain_5(self):
        url = Url("https://user:pass.banana@g1.globo.com/rj")
        self.assertEqual(url.domain, "g1.globo.com")

    def test_url_user_6(self):
        url = Url("https://user:pass.banana@g1.globo.com/rj")
        self.assertEqual(url.user, "user")

if __name__ == '__main__':
    unittest.main()
