import unittest
from dojo import decode_way, greater


class DojoTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(decode_way("1"), 1)

    def test_case_2(self):
        self.assertEqual(decode_way("2"), 1)

    def test_case_11(self):
        self.assertEqual(decode_way("11"), 2)

    def test_case_22(self):
        self.assertEqual(decode_way("22"), 2)

    def test_case_27(self):
        self.assertEqual(decode_way("27"), 1)

    def test_case_226(self):
        self.assertEqual(decode_way("226"), 3)

    def test_case_227(self):
        self.assertEqual(decode_way("227"), 2)

    def test_case_greater(self):
        self.assertEqual(greater("27"), 0)

    def test_case_greater(self):
        self.assertEqual(greater("26"), 1)


if __name__ == '__main__':
    unittest.main()
