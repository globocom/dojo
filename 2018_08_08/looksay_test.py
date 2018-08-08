import unittest
from looksay import main


class LookSayTest(unittest.TestCase):
    def test_one_digit_number_1(self):
        self.assertEqual(main(1),11)
    def test_one_digit_number_2(self):
        self.assertEqual(main(2),12)
    def test_one_digit_number_0(self):
        self.assertEqual(main(0),10)
    def test_two_digit_number_11(self):
        self.assertEqual(main(11), 21)
    def test_two_digit_number_12(self):
        self.assertEqual(main(12), 1112)
    def test_two_digit_number_13(self):
        self.assertEqual(main(13), 1113)
    def test_three_digit_number_11(self):
        self.assertEqual(main(11), 21)

if __name__ == '__main__':
    unittest.main()