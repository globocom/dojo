import unittest
from dojo import main
from dojo import parser_string

class DojoTest(unittest.TestCase):
    def test_olamundo(self):
        matrix = [
            ['o','m','d'],
            ['l','u','o'],
            ['a','n','!']
        ]
        self.assertEqual(main(matrix), 'olamundo!')

    def test_helloworld(self):
        matrix = [
            ['h','o','l'],
            ['e','w','d'],
            ['l','o','!'],
            ['l','r','!']
        ]
        self.assertEqual(main(matrix), 'helloworld!!')

    def test_olavey(self):
        matrix = [
            ['o','v'],
            ['l','e'],
            ['a','y'],
        ]
        self.assertEqual(main(matrix), 'olavey')

    def test_olaalphanumericoespaco(self):
        matrix = [
            ['o','!'],
            ['l','e'],
            ['a','y'],
        ]
        self.assertEqual(main(matrix), 'ola ey')

    def test_olastring(self):
        string = "ola!ey"
        self.assertEqual(parser_string(string),'ola ey')

    def test_olastring_2(self):
        string = "olavey"
        self.assertEqual(parser_string(string),'olavey')

    def test_olastring_3(self):
        string = "olave!y"
        self.assertEqual(parser_string(string),'olave y')

    def test_olastring_3(self):
        string = "olave!y!"
        self.assertEqual(parser_string(string),'olave y!')

    

if __name__ == '__main__':
    unittest.main()
    
