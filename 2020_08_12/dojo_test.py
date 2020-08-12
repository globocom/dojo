import unittest
from dojo import get_last_day, call_buses,main


class DojoTest(unittest.TestCase):
    def test_get_last_day_1(self):
        self.assertEqual(get_last_day(10,2), 10)

    def test_get_last_day_2(self):
        self.assertEqual(get_last_day(10,7), 7)

    def test_get_last_day_3(self):
        self.assertEqual(get_last_day(7,3), 6)

    def test_call_buses_1(self):
        self.assertEqual(call_buses(10,[3,7,2]), 6)
    
    def test_call_buses_2(self):
        self.assertEqual(call_buses(100,[11,10,5,50]), 99)
    
    def test_call_buses_3(self):
        self.assertEqual(call_buses(1,[1]), 1)

    def test_main(self):
        self.assertEqual(main(1,1,[1]), 1)

if __name__ == '__main__':
    unittest.main()

#Ingrid - Sami - Paulo - Elen - Juan - Tiago - Allan