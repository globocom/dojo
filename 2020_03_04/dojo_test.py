import unittest
from dojo import parse_input, convert_time_to_seconds, convert_timestamp_to_seconds


class DojoTest(unittest.TestCase):
    def test_get_info_1(self):
        self.assertEqual(parse_input("Sun 10 May 2015 13:54:36 -0700"),["10","May","2015","13","54","36","-0700"])
    def test_get_info_2(self):
        self.assertEqual(parse_input("Sun 14 May 2015 13:54:36 -0700"),["14","May","2015","13","54","36","-0700"])
    def test_get_info_3(self):
        self.assertEqual(parse_input("Sun 14 May 2015 20:54:36 -0700"),["14","May","2015","20","54","36","-0700"])
    def test_time_convert_to_sec_1(self):
        self.assertEqual(convert_time_to_seconds(["13","54","36"]), 13*3600+54*60+36)
    def test_time_convert_to_sec_2(self):
        self.assertEqual(convert_time_to_seconds(["12", "54", "39"]), 12*3600+54*60+39)
    def test_time_convert_to_sec_3(self):
        self.assertEqual(convert_time_to_seconds(["01", "54", "39"]), 1*3600+54*60+39)
    def test_timestamp_convert_to_sec_1(self):
        self.assertEqual(convert_timestamp_to_seconds("-0700"), -25200)
    def test_timestamp_convert_to_sec_2(self):
        self.assertEqual(convert_timestamp_to_seconds("-0530"), -19800)
    def test_timestamp_convert_to_sec_3(self):
        self.assertEqual(convert_timestamp_to_seconds("-0300"), -10800)


if __name__ == '__main__':
    unittest.main()
