import unittest
from dojo import get_tag

class ScrapperTest(unittest.TestCase):
    def test_get_img(self):
        body = "<img/>"
        self.assertEqual(get_tag("img",body), ["<img/>"])

    def test_get_2_imgs(self):
        body = "<img/><img/>"
        self.assertEqual(get_tag("img",body), ["<img/>","<img/>"])
    
    def test_get_3_imgs(self):
        body = "<img/><img/><img/>"
        self.assertEqual(get_tag("img",body), ["<img/>","<img/>","<img/>"])

    def test_img_wit_attr(self):
        body = "<img src='foo.bar'/>"
        self.assertEqual(get_tag("img",body), ["<img src='foo.bar'/>"])
    
    def test_img_wit_2attr(self):
        body = "<img src='foo.bar' alt='bar.foo'/>"
        self.assertEqual(get_tag("img",body), ["<img src='foo.bar' alt='bar.foo'/>"])

    # def test_get_1_div(self):
    #     body = "<div/>"
    #     self.assertEqual(get_tag("div",body), ["<div/>"])

    # def test_get_2_div(self):
    #     body = "<div/><div/>"
    #     self.assertEqual(get_tag("div",body), ["<div/>","<div/>"])


if __name__ == '__main__':
    unittest.main()
