import unittest
from dojo import main
from dojo import get_days
from dojo import invert_number, is_beatiful_day

class DojoTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(20,21, 6), 1)

    def test_main_2(self):
        self.assertEqual(main(20,23, 2), 2)

    def test_main_3(self):
        self.assertEqual(main(20,24, 2), 3)

    def test_get_days(self):
        self.assertEqual(get_days(20, 23), [20, 21, 22, 23])

    def test_get_days_2(self):
        self.assertEqual(get_days(20, 24), [20, 21, 22, 23, 24])
    
    def test_get_days_3(self):
        self.assertEqual(get_days(10, 15), [10, 11, 12, 13, 14, 15])
    
    def test_invert_number(self):
        self.assertEqual(invert_number(10), 1)

    def test_invert_number_2(self):
        self.assertEqual(invert_number(15), 51)

    def test_invert_number_3(self):
        self.assertEqual(invert_number(22), 22)

    def test_is_beatiful_day(self):
        self.assertEqual(is_beatiful_day(20, 6), True)

    def test_is_beatiful_day_2(self):
        self.assertEqual(is_beatiful_day(21, 6), False)

    def test_is_beatiful_day_3(self):
        self.assertEqual(is_beatiful_day(31, 3), True)

    def test_is_beatiful_day_4(self):
        self.assertEqual(is_beatiful_day(24, 6), True)
    

if __name__ == '__main__':
    unittest.main()
