import App.Geometry as Geometry


class MobileRobot:
    def __init__(self):
        self.__position = Geometry.Point()
        self.__orientation = Geometry.Orientation.INVALID

    def get_position(self):
        return self.__position

    def set_position(self, point):
        self.__position = point

    def get_orientation(self):
        return self.__orientation

    def set_orientation(self, orientation):
        self.__orientation = orientation


class Board:
    def __init__(self, bottom_left=Geometry.Point(), top_right=Geometry.Point()):
        self.__bottom_left = bottom_left
        self.__top_right = top_right

    def get_bottom_left(self):
        return self.__bottom_left

    def set_bottom_left(self, point):
        self.__bottom_left = point

    def get_top_right(self):
        return self.__top_right

    def set_top_right(self, point):
        self.__top_right = point

    def is_valid(self):
        return all([
            self.__bottom_left.is_valid(),
            self.__top_right.is_valid()
        ])

    def is_valid_position(self, position):
        return all([
            position.is_valid(),
            self.is_valid(),
            self.__bottom_left.get_x() <= position.get_x(),
            self.__bottom_left.get_y() <= position.get_y(),
            self.__top_right.get_x() >= position.get_x(),
            self.__top_right.get_y() >= position.get_y()
        ])

    def __eq__(self, other):
        return all([
            self.__bottom_left == self.__bottom_left,
            self.__top_right == self.__top_right
        ])


class WorldModel:
    def __init__(self):
        self.__robot = MobileRobot()
        self.__board = Board(Geometry.Point(0, 0), Geometry.Point(4, 4))

    def get_robot(self):
        return self.__robot

    def get_board(self):
        return self.__board
