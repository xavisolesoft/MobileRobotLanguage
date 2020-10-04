import unittest
import App.Geometry as Geometry


class OrientationTestCase(unittest.TestCase):
    def test_is_valid(self):
        for orientation in Geometry.Orientation:
            if orientation == Geometry.Orientation.INVALID:
                self.assertFalse(orientation.is_valid())
            else:
                self.assertTrue(orientation.is_valid())

    def test_to_normalized_vector(self):
        self.assertEqual(Geometry.Point(), Geometry.Orientation.INVALID.to_normalized_vector())
        self.assertEqual(Geometry.Point(0, 1), Geometry.Orientation.NORTH.to_normalized_vector())
        self.assertEqual(Geometry.Point(1, 0), Geometry.Orientation.EAST.to_normalized_vector())
        self.assertEqual(Geometry.Point(0, -1), Geometry.Orientation.SOUTH.to_normalized_vector())
        self.assertEqual(Geometry.Point(-1, 0), Geometry.Orientation.WEST.to_normalized_vector())

    def test_get_left_rotated(self):
        self.assertEqual(Geometry.Orientation.INVALID, Geometry.Orientation.INVALID.get_left_rotated())
        self.assertEqual(Geometry.Orientation.WEST, Geometry.Orientation.NORTH.get_left_rotated())
        self.assertEqual(Geometry.Orientation.SOUTH, Geometry.Orientation.WEST.get_left_rotated())
        self.assertEqual(Geometry.Orientation.EAST, Geometry.Orientation.SOUTH.get_left_rotated())
        self.assertEqual(Geometry.Orientation.NORTH, Geometry.Orientation.EAST.get_left_rotated())

    def test_get_right_rotated(self):
        self.assertEqual(Geometry.Orientation.INVALID, Geometry.Orientation.INVALID.get_right_rotated())
        self.assertEqual(Geometry.Orientation.EAST, Geometry.Orientation.NORTH.get_right_rotated())
        self.assertEqual(Geometry.Orientation.NORTH, Geometry.Orientation.WEST.get_right_rotated())
        self.assertEqual(Geometry.Orientation.WEST, Geometry.Orientation.SOUTH.get_right_rotated())
        self.assertEqual(Geometry.Orientation.SOUTH, Geometry.Orientation.EAST.get_right_rotated())


class PointTestCase(unittest.TestCase):
    def test_default_constructor(self):
        point = Geometry.Point()
        self.assertEqual(Geometry.Point.INVALID_POSITION, point.get_x())
        self.assertEqual(Geometry.Point.INVALID_POSITION, point.get_y())

    def test_x_y_constructor(self):
        x = 2
        y = 3
        point = Geometry.Point(x, y)

        self.assertEqual(x, point.get_x())
        self.assertEqual(y, point.get_y())

    def test_eq_operator(self):
        x = 10
        y = -25

        self.assertTrue(Geometry.Point() == Geometry.Point())
        self.assertTrue(Geometry.Point(x, y) == Geometry.Point(x, y))
        self.assertFalse(Geometry.Point() == Geometry.Point(x, y))
        self.assertFalse(Geometry.Point(x, y) == Geometry.Point(x + 1, y + 1))

    def test_add_operator_invalid_values(self):
        x = -100
        y = 5

        self.assertTrue(Geometry.Point(), Geometry.Point() + Geometry.Point())
        self.assertTrue(Geometry.Point(), Geometry.Point(x) + Geometry.Point())
        self.assertTrue(Geometry.Point(), Geometry.Point(Geometry.Point.INVALID_POSITION, y) + Geometry.Point(x))
        self.assertTrue(Geometry.Point(), Geometry.Point(Geometry.Point.INVALID_POSITION, y) + Geometry.Point())
        self.assertTrue(Geometry.Point(x + x), Geometry.Point(x) + Geometry.Point(x))
        self.assertTrue(Geometry.Point(Geometry.Point.INVALID_POSITION, y),
                        Geometry.Point(Geometry.Point.INVALID_POSITION, y) + Geometry.Point(Geometry.Point.INVALID_POSITION, y))

    def test_add_operator_valid_values(self):
        x = -100
        y = 200

        self.assertTrue(Geometry.Point(x + x, y + y), Geometry.Point(x, y) + Geometry.Point(x, y))
        self.assertTrue(Geometry.Point(0, 0), Geometry.Point(x, y) + Geometry.Point(-x, -y))

    def test_set_get_x(self):
        x1 = 56
        x2 = 45
        point = Geometry.Point()

        point.set_x(x1)
        self.assertEqual(x1, point.get_x())
        point.set_x(x2)
        self.assertEqual(x2, point.get_x())

    def test_set_get_y(self):
        y1 = 34
        y2 = -500
        point = Geometry.Point()

        point.set_y(y1)
        self.assertEqual(y1, point.get_y())
        point.set_y(y2)
        self.assertEqual(y2, point.get_y())

    def test_is_valid(self):
        x = 57
        y = 90

        self.assertFalse(Geometry.Point().is_valid())
        self.assertFalse(Geometry.Point(x).is_valid())
        self.assertFalse(Geometry.Point(Geometry.Point.INVALID_POSITION, y).is_valid())
        self.assertTrue(Geometry.Point(x, y))


if __name__ == '__main__':
    unittest.main()
