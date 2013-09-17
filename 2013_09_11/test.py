import unittest
from largest_sum import find_largest_sum, sum_interval, build_matrix


class LargestSumTestCase(unittest.TestCase):

    def test_list_1_return_0_0(self):
        sample_list = [1]
        response = find_largest_sum(sample_list)
        self.assertEqual(response, (0, 0))

    #def test_list_1_1_return_0_1(self):
     #   sample_list = [1, 1]
      #  response = find_largest_sum(sample_list)
       # self.assertEqual(response, (0, 1))

    def test_list_negative_numbers(self):
        sample_list = [-1]*10
        begin, end = find_largest_sum(sample_list)
        self.assertEqual(begin, end)

    def test_sum_interval(self):
        sample_list = [1, 2, 3, 4]
        total = sum_interval(sample_list, 0, 2)
        self.assertEqual(total, 6)

    def test_sum_interval_another_example(self):
        sample_list = [1, 2, 3, 4, 5, 6]
        total = sum_interval(sample_list, 0, 1)
        self.assertEqual(total, 3)

    def test_build_matrix(self):
        sample_list = [1, 2, -1]
        expected_response = [
            [1, 3, 2],
            [2, 1],
            [-1]
        ]
        self.assertEqual(build_matrix(sample_list), expected_response)



unittest.main()