import unittest
from dojo import *


class DojoTest(unittest.TestCase):
    def test_validate1(self):
        self.assertTrue(validate("abcdef", 609043))
    def test_validate2(self):
        self.assertTrue(validate("pqrstuv", 1048970))
    def test_validate3(self):
        self.assertFalse(validate("aaaaaa", 42))


    def test_main(self):
        self.assertEquals(main("abcdef"), 609043)
    def test_main2(self):
        self.assertEquals(main("pqrstuv"), 1048970)
    def test_main3(self):
        self.assertEquals(main("iwrupvqb"), 346386)

    def test_main4(self):
        self.assertEquals(main("iwrupvqb", 6), 9958218)


# "abcdef" + 609043, 
    # because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...)
# "pqrstuv" + 1048970
    # pqrstuv1048970 looks like 000006136ef....

if __name__ == '__main__':
    unittest.main()


# hello world
##
## import hashlib
## print(hashlib.md5("whatever your string is".encode('utf-8')).hexdigest())


