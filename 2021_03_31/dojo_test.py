import unittest
from dojo import main, encode_string


class DojoTest(unittest.TestCase):     
    def test_1(self):
        self.assertEqual(main("5a2bc", 8), "aaaaabbc") 
    def test_2(self):
        self.assertEqual(main("5a2bc", 7), "unfeasible")
    def test_3(self):
        self.assertEqual(main("asdf4x", 50), "asdfxxxx")

    def test_4(self):   
        self.assertEqual(encode_string("aaaaabbc"), "5a2bc")
    def test_5(self):   
        self.assertEqual(encode_string("asdfxxxx"), "asdf4x")
    def test_6(self):   
        self.assertEqual(encode_string("abcd"), "abcd")


#    def test_1(self):
#        self.assertEqual(main("5a2bc", 8), "aaaaabbc")
#    def test_2(self):
#        self.assertEqual(main("5a2bc", 7), "unfeasible")
#    def test_3(self):
#        self.assertEqual(main("asdf4x", 50), "asdfxxxx")
#    def test_4(self):
#        self.assertEqual(main("asjkdf10000000000kz", 1000000), "unfeasible")


if __name__ == '__main__':
    unittest.main()
