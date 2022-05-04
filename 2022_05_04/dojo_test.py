import unittest
from dojo import *


INPUT = "ffykfhsq"

TEST_INPUT = "abc3231929"

class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(main())

    def test_compute_hash_1(self):
        self.assertEqual(compute_hash("abc3231929"), "00000155f8105dff7f56ee10fa9b9abd")

    def test_compute_hash_2(self):
        self.assertEqual(compute_hash("abc5017308"), "000008f82c5b3924a1ecbebf60344e00")
    
    def test_compute_hash_3(self):
        self.assertEqual(compute_hash("abc5278568"), "00000f9a2c309875e05c5a5d09f1b8c4")

    def test_process(self):
        self.assertEqual(process("abc"), "18f47a30")

    def test_process_real(self):
        self.assertEqual(process("ffykfhsq"), "c6697b55")

    def test_process_2(self):
        self.assertEqual(process_2("abc"), "05ace8e3")

    def test_process_2(self):
        self.assertEqual(process_2("ffykfhsq"), "8c35d1ab")

if __name__ == '__main__':
    unittest.main()
