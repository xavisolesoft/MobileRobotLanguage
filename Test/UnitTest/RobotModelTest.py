import unittest
import sys
import os.path

sys.path.extend([os.path.dirname(os.path.abspath(__file__)) + "/../.."])
import Definitions
sys.path.extend([Definitions.APP_PATH])

import App.Geometry as Geometry
import App.RobotModel as RobotModel


class MobileRobotTestCase(unittest.TestCase):
    def test_default_constructor(self):
        robot = RobotModel.MobileRobot()

        self.assertFalse(robot.get_position().is_valid())
        self.assertEqual(Geometry.Point(Geometry.Point.INVALID_POSITION, Geometry.Point.INVALID_POSITION),
                         robot.get_position())
        self.assertFalse(robot.get_orientation().is_valid())

    def test_set_get_position(self):
        point = Geometry.Point(69, -90)
        robot = RobotModel.MobileRobot()

        robot.set_position(point)

        self.assertEqual(point, robot.get_position())

    def test_set_get_orientation(self):
        orientation = Geometry.Orientation.SOUTH
        robot = RobotModel.MobileRobot()

        robot.set_orientation(orientation)

        self.assertEqual(orientation, robot.get_orientation())


class BoardTestCase(unittest.TestCase):
    FULL_INVALID_POINT = Geometry.Point(Geometry.Point.INVALID_POSITION,
                                        Geometry.Point.INVALID_POSITION)
    VALID_POINT = Geometry.Point(0, 0)
    INVALID_POINT = Geometry.Point()
    VALID_BOARD = RobotModel.Board(Geometry.Point(0, 0),
                                   Geometry.Point(10, 10))

    def test_default_constructor(self):
        board = RobotModel.Board()

        self.assertFalse(board.is_valid())
        self.assertEqual(RobotModel.Board(self.FULL_INVALID_POINT, self.FULL_INVALID_POINT),
                         board)

    def test_bottom_left_constructor(self):
        bottom_left = Geometry.Point(0, 0)
        board = RobotModel.Board(bottom_left)

        self.assertFalse(board.is_valid())
        self.assertEqual(RobotModel.Board(bottom_left, self.FULL_INVALID_POINT),
                         board)

    def test_bottom_left_top_right_constructor(self):
        bottom_left = Geometry.Point(0, 0)
        top_right = Geometry.Point(5, 5)
        board = RobotModel.Board(bottom_left)

        self.assertFalse(board.is_valid())
        self.assertEqual(RobotModel.Board(bottom_left, top_right),
                         board)

    def test_set_get_bottom_left_constructor(self):
        bottom_left = Geometry.Point(-10, -10)
        board = RobotModel.Board()

        board.set_bottom_left(bottom_left)

        self.assertEqual(bottom_left, board.get_bottom_left())

    def test_set_get_top_right_constructor(self):
        top_right = Geometry.Point(10, 10)
        board = RobotModel.Board()

        board.set_bottom_left(top_right)

        self.assertEqual(top_right, board.get_bottom_left())

    def is_valid(self):
        self.assertFalse(RobotModel.Board(self.FULL_INVALID_POINT, self.FULL_INVALID_POINT).is_valid())
        self.assertFalse(RobotModel.Board(self.VALID_POINT, self.FULL_INVALID_POINT).is_valid())
        self.assertTrue(RobotModel.Board(self.VALID_POINT, self.VALID_POINT).is_valid())

    def test_is_valid_position_not_valid_board(self):
        invalid_board = RobotModel.Board()

        self.assertFalse(invalid_board.is_valid_position(self.VALID_POINT))
        self.assertFalse(invalid_board.is_valid_position(self.INVALID_POINT))

    def test_is_valid_position_not_valid_point(self):
        valid_board = RobotModel.Board(self.VALID_POINT, self.VALID_POINT)

        self.assertFalse(valid_board.is_valid_position(self.INVALID_POINT))

    def test_is_valid_position_outside_board(self):
        self.VALID_BOARD = RobotModel.Board(Geometry.Point(0, 0),
                                            Geometry.Point(10, 10))
        out_left_point = Geometry.Point(self.VALID_BOARD.get_bottom_left().get_x() - 1,
                                        self.VALID_BOARD.get_bottom_left().get_y())
        out_bottom_point = Geometry.Point(self.VALID_BOARD.get_bottom_left().get_x(),
                                          self.VALID_BOARD.get_bottom_left().get_y() - 1)
        out_right_point = Geometry.Point(self.VALID_BOARD.get_top_right().get_x() + 1,
                                         self.VALID_BOARD.get_top_right().get_y())
        out_top_point = Geometry.Point(self.VALID_BOARD.get_top_right().get_x(),
                                       self.VALID_BOARD.get_top_right().get_y() + 1)
        out_bottom_left_point = Geometry.Point(self.VALID_BOARD.get_bottom_left().get_x() - 1,
                                               self.VALID_BOARD.get_bottom_left().get_y() - 1)
        out_top_left_point = Geometry.Point(self.VALID_BOARD.get_bottom_left().get_x() - 1,
                                            self.VALID_BOARD.get_top_right().get_y() + 1)
        out_top_right_point = Geometry.Point(self.VALID_BOARD.get_top_right().get_x() + 1,
                                             self.VALID_BOARD.get_top_right().get_y() + 1)
        out_bottom_right_point = Geometry.Point(self.VALID_BOARD.get_top_right().get_x() + 1,
                                                self.VALID_BOARD.get_bottom_left().get_y() - 1)

        self.assertFalse(self.VALID_BOARD.is_valid_position(out_left_point))
        self.assertFalse(self.VALID_BOARD.is_valid_position(out_bottom_point))
        self.assertFalse(self.VALID_BOARD.is_valid_position(out_right_point))
        self.assertFalse(self.VALID_BOARD.is_valid_position(out_top_point))
        self.assertFalse(self.VALID_BOARD.is_valid_position(out_bottom_left_point))
        self.assertFalse(self.VALID_BOARD.is_valid_position(out_top_left_point))
        self.assertFalse(self.VALID_BOARD.is_valid_position(out_top_right_point))
        self.assertFalse(self.VALID_BOARD.is_valid_position(out_bottom_right_point))

    def test_is_valid_position_in_margin_board(self):
        self.VALID_BOARD = RobotModel.Board(Geometry.Point(0, 0),
                                            Geometry.Point(10, 10))
        left_margin_point = Geometry.Point(self.VALID_BOARD.get_bottom_left().get_x(),
                                           self.VALID_BOARD.get_bottom_left().get_y() + 1)
        bottom_margin_point = Geometry.Point(self.VALID_BOARD.get_bottom_left().get_x() + 1,
                                             self.VALID_BOARD.get_bottom_left().get_y())
        right_margin_point = Geometry.Point(self.VALID_BOARD.get_top_right().get_x(),
                                            self.VALID_BOARD.get_top_right().get_y() - 1)
        top_margin_point = Geometry.Point(self.VALID_BOARD.get_top_right().get_x() - 1,
                                          self.VALID_BOARD.get_top_right().get_y())
        bottom_left_margin_point = self.VALID_BOARD.get_bottom_left()
        top_left_margin_point = self.VALID_BOARD.get_top_right()
        top_right_margin_point = self.VALID_BOARD.get_top_right()
        bottom_right_margin_point = self.VALID_BOARD.get_bottom_left()

        self.assertTrue(self.VALID_BOARD.is_valid_position(left_margin_point))
        self.assertTrue(self.VALID_BOARD.is_valid_position(bottom_margin_point))
        self.assertTrue(self.VALID_BOARD.is_valid_position(right_margin_point))
        self.assertTrue(self.VALID_BOARD.is_valid_position(top_margin_point))
        self.assertTrue(self.VALID_BOARD.is_valid_position(bottom_left_margin_point))
        self.assertTrue(self.VALID_BOARD.is_valid_position(top_left_margin_point))
        self.assertTrue(self.VALID_BOARD.is_valid_position(top_right_margin_point))
        self.assertTrue(self.VALID_BOARD.is_valid_position(bottom_right_margin_point))

    def test_is_valid_position_inside_point(self):
        self.VALID_BOARD = RobotModel.Board(Geometry.Point(0, 0),
                                            Geometry.Point(10, 10))
        inside_point = Geometry.Point(self.VALID_BOARD.get_bottom_left().get_x() + 1,
                                      self.VALID_BOARD.get_bottom_left().get_y() + 1)

        self.assertTrue(self.VALID_BOARD.is_valid_position(inside_point))


if __name__ == '__main__':
    unittest.main()
