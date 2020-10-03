import unittest
import dojo


class DojoTest(unittest.TestCase):
    def test_sala_one_one(self):
        self.assertEqual(
            dojo.main([(0, 0), (0, 1), (1, 0), (1, 1), (1, 1)]),
            1
        )

    def test_sala_two_one(self):
        self.assertEqual(
            dojo.main([(0, 0), (0, 2), (1, 0), (1, 2), (1, 1)]),
            2
        )

    def test_sala_two_two(self):
        self.assertEqual(
            dojo.main([(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)]),
            4
        )

    def test_sala_two_two_size_2(self):
        self.assertEqual(
            dojo.main([(0, 0), (0, 2), (2, 0), (2, 2), (1, 2)]),
            2
        )
    
    def test_sala_two_two_size_2half(self):
        self.assertEqual(
            dojo.main([(0, 0), (2, 0), (0, 1), (1, 1), (1, 1)]),
            2
        )

    def test_sala_two_two_size_1half(self):
        self.assertEqual(
            dojo.main([(0, 0), (2, 0), (0, 1), (1, 1), (2, 1)]),
            1
        )


if __name__ == '__main__':
    unittest.main()
