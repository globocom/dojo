import unittest
from dojo import main, get_extensive_list

class DojoTest(unittest.TestCase):
    def test_unit_extensive_to_number1(self):
        self.assertEqual(main("Um"),1)

    def test_unit_extensive_to_number3(self):
        self.assertEqual(main("Três"), 3)

    def test_unit_extensive_to_number_lower_case(self):
        self.assertEqual(main("dois"), 2)

    def test_extensive_decimal_20_to_number_lower_case(self):
        self.assertEqual(main("vinte"), 20)

    def test_extensive_decimal_30_to_number_lower_case(self):
        self.assertEqual(main("trinta"), 30)

    def test_extensive_decimal_40_to_number_lower_case(self):
        self.assertEqual(main("quarenta"), 40)

    def test_extensive_decimal_42_to_number_lower_case(self):
        self.assertEqual(get_extensive_list("quarenta e dois"), ["quarenta", "dois"])

    def test_extensive_decimal_52_to_number_lower_case(self):
        self.assertEqual(get_extensive_list("ciquenta e dois"), ["ciquenta", "dois"])

    def test_extensive_decimal_62_to_number_lower_case(self):
        self.assertEqual(get_extensive_list("sessenta e dois"), ["sessenta", "dois"])

if __name__ == '__main__':
    unittest.main()
