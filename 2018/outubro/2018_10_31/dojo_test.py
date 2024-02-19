import unittest
from dojo import main, next_position


class DojoTest(unittest.TestCase):
    def test_one_one(self):
        self.assertEqual(main(1, 1), [[1]])

    def test_one_two(self):
        self.assertEqual(main(1, 2), [[1, 2]])

    def test_one_three(self):
        self.assertEqual(main(1, 3), [[1, 2, 3]])

    def test_two_one(self):
        self.assertEqual(main(2, 1), [
            [1],
            [2]
        ])

    # def test_two_two(self):
    #     self.assertEqual(main(2, 2), [
    #         [1,2],
    #         [4,3]
    #     ])

    def test_next_position_one_two(self):
        self.assertEqual(next_position([[1,None]], (0,0)), (0,1))

    def test_next_position_two_two(self):
        self.assertEqual(next_position([[1,2],[None,None]], (0,1)), (1,1))

    # def test_next_position_two_two(self):
    #     self.assertEqual(next_position([[1,2],[None,3]], (1,1)), (1,0))


if __name__ == '__main__':
    unittest.main()
