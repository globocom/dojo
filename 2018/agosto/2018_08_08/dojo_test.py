import unittest
from dojo import main


class DojoTest(unittest.TestCase):
    def test_number_divisible_by_3(self):
        self.assertEqual(main(3), "Fizz")

    def test_number_is_not_divisible_by_3(self):
        self.assertEqual(main(2), 2)

    def test_number_is_divisible_by_5(self):
        self.assertEqual(main(5), "Buzz")
        self.assertEqual(main(10), "Buzz")

    def test_number_is_divisible_by_5_and_3(self):
        self.assertEqual(main(15), "FizzBuzz")
        self.assertEqual(main(30), "FizzBuzz")



if __name__ == '__main__':
    unittest.main()