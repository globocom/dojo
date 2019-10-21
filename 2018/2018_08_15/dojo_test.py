import unittest
from dojo import Robot


class RobotTest(unittest.TestCase):
    def test_initialization(self):
        robot = Robot(7, 3, 'north')
        self.assertEqual(robot.x, 7)
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.direction, 'north')

    def test_get_position(self):
        robot = Robot(7, 3, 'north')
        self.assertEqual(robot.get_position(), (7, 3, 'north'))

    def test_turn_right(self):
        robot = Robot(7, 3, 'north')
        self.assertEqual(robot.turn_right(), 'east')
        self.assertEqual(robot.turn_right(), 'south')
        self.assertEqual(robot.turn_right(), 'west')
        self.assertEqual(robot.turn_right(), 'north')

    def test_turn_left(self):
        robot = Robot(7, 3, 'north')
        self.assertEqual(robot.turn_left(), 'west')
        self.assertEqual(robot.turn_left(), 'south')
        self.assertEqual(robot.turn_left(), 'east')
        self.assertEqual(robot.turn_left(), 'north')

    def test_advance(self):
        robot = Robot(7, 3, 'north')
        self.assertEqual(robot.advance(), (7, 4, 'north'))
        self.assertEqual(robot.advance(), (7, 5, 'north'))

if __name__ == '__main__':
    unittest.main()