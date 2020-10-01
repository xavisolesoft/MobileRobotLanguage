from enum import Enum


class Orientation(Enum):
    INVALID = 0
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    def is_valid(self):
        return self != self.INVALID


class Point:
    INVALID_POS = -1

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
        return self.INVALID_POS not in [self.__x, self.__y]
