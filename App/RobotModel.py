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
    MIN_POSITION = Geometry.Point(0, 0)
    MAX_POSITION = Geometry.Point(4, 4)

    def is_valid_position(self, position):
        return all([
            self.MIN_POSITION.get_x() <= position.get_x(),
            self.MIN_POSITION.get_y() <= position.get_y(),
            self.MAX_POSITION.get_x() >= position.get_x(),
            self.MAX_POSITION.get_y() >= position.get_y()
        ])


class WorldModel:
    def __init__(self):
        self.__robot = MobileRobot()
        self.__board = Board()

    def get_robot(self):
        return self.__robot

    def get_board(self):
        return self.__board


world_model = WorldModel()
