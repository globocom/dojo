import unittest
from dojo import main, check_sum

class DojoTest(unittest.TestCase):
    def test_check_sum1(self):
        self.assertTrue(check_sum(2, 7, 9))

    def test_check_sum2(self):
        self.assertFalse(check_sum(3, 7, 9))

    def test_check_sum3(self):
        self.assertTrue(check_sum(2, 8, 10))


    def test_main1(self):
        self.assertEqual(main([2,7,11,15], 9), [0,1])

    def test_main2(self):
        self.assertEqual(main([2,7,11,15], 18), [1,2])

    def test_main3(self):
        self.assertEqual(main([2,7,11,15], 17), [0,3])


if __name__ == '__main__':
    unittest.main()

#         0,1, 2, 3
# nums = [2,7,11,15]
# target = 18
# output [1,2]


