import unittest
from dojo import Robot


class DojoTest(unittest.TestCase):
    def test_t_right(self):
        robot = Robot("T")
        self.assertEqual(robot.turn_right(), "R")

    def test_r_down(self):
        robot = Robot("R")
        self.assertEqual(robot.turn_right(), "D")

    def test_r_left(self):
        robot = Robot("D")
        self.assertEqual(robot.turn_right(), "L")

    def test_r_top(self):
        robot = Robot("L")
        self.assertEqual(robot.turn_right(), "T")

    def test_l_left(self):
        robot = Robot("T")
        self.assertEqual(robot.turn_left(), "L")

    def test_l_top(self):
        robot = Robot("R")
        self.assertEqual(robot.turn_left(), "T")

    def test_l_right(self):
        robot = Robot("D")
        self.assertEqual(robot.turn_left(), "R")

    def test_l_down(self):
        robot = Robot("L")
        self.assertEqual(robot.turn_left(), "D")


if __name__ == '__main__':
    unittest.main()
