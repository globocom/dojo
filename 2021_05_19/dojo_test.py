import unittest
from dojo import main, function_right, function_in


class DojoTest(unittest.TestCase):
    def test_function_right1(self):
        self.assertEqual(function_right("1492", "2013"), 0)

    def test_function_right2(self):
        self.assertEqual(function_right("1234", "1234"), 4)

    def test_function_right3(self):
        self.assertEqual(function_right("1235", "1342"), 1)

    def test_function_wrongs1(self):
        self.assertEqual(function_in("1492", "2013"), 2)

    def test_function_wrongs2(self):
        self.assertEqual(function_in("1492", "1865"), 1)
    
    def test_function_wrongs3(self):
        self.assertEqual(function_in("1492", "1234"), 3)
    
    def test_function_main1(self):
        self.assertEqual(main("1492", "2013"), "0-2")
    
    def test_function_main2(self):
        self.assertEqual(main("1492", "1865"), "1-0")
    
    def test_function_main3(self):
        self.assertEqual(main("1492", "1234"), "1-2")
    
    def test_function_main4(self):
        self.assertEqual(main("1492", "4321"), "0-3")

    def test_function_main2(self):
        self.assertEqual(main("1492", "1492"), "4-0")


    # 2013 1865 1234 4321 7491

if __name__ == '__main__':
    unittest.main()


# Lara -> Carreira -> Joao -> Ildefonso
# Duas funçoes 

