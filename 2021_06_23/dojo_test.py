import unittest
from dojo import main


class DojoTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main([2,3,1,1,4]), 2)

    def test_2(self):
        self.assertEqual(main([2,3,0,1,4]), 2)

    def test_3(self):
        self.assertEqual(main([1,1,4,1,4]), 3)

    def test_4(self):
        self.assertEqual(main([3,1,3,1,1,4]), 2)




if __name__ == '__main__':
    unittest.main()

