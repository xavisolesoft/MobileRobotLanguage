from enum import Enum
import sys


class Orientation(Enum):
    INVALID = 0
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    def is_valid(self):
        return self != self.INVALID

    def to_normalized_vector(self):
        switcher = {
            Orientation.INVALID: Point(),
            Orientation.NORTH: Point(0, 1),
            Orientation.EAST: Point(1, 0),
            Orientation.SOUTH: Point(0, -1),
            Orientation.WEST: Point(-1, 0)
        }
        return switcher.get(self)

    def get_left_rotated(self):
        if self is Orientation.INVALID:
            return Orientation.INVALID

        return self.__get_valid_left_rotated()

    def get_right_rotated(self):
        if self is Orientation.INVALID:
            return Orientation.INVALID

        return self.__get_valid_right_rotated()

    def __get_valid_left_rotated(self):
        rotated = self.value - 1
        if rotated < 1:
            rotated = 4

        return Orientation(rotated)

    def __get_valid_right_rotated(self):
        rotated = self.value + 1
        if rotated > 4:
            rotated = 1

        return Orientation(rotated)


class Point:
    INVALID_POS = -sys.maxsize

    def __init__(self, x=INVALID_POS, y=INVALID_POS):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def is_valid(self):
        return Point.INVALID_POS not in [self.__x, self.__y]

    def __eq__(self, other):
        return all([self.__x == other.__x,
                    self.__y == other.__y])

    def __add__(self, other):
        return Point(self.__add_coordinate(self.__x, other.__x),
                     self.__add_coordinate(self.__y, other.__y))

    @staticmethod
    def __add_coordinate(self_position, other_position):
        if Point.INVALID_POS in [self_position, other_position]:
            return Point.INVALID_POS

        return self_position + other_position
