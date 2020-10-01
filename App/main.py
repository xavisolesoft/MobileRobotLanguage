import sys
from enum import Enum

INVALID_COMMAND_ID = -1


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


class RobotCommandRequest:
    INVALID_COMMAND_ID = -1

    def __init__(self):
        self.__command_id = INVALID_COMMAND_ID

    def get_id(self):
        return self.__command_id

    def set_id(self, command_id):
        self.__command_id = command_id

    def is_valid(self):
        return self.__command_id != INVALID_COMMAND_ID


class RobotCommandResponse:
    INVALID_ERROR_MESSAGE = "INVALID ERROR MESSAGE"

    def __init__(self):
        self.__command_id = INVALID_COMMAND_ID
        self.__error_message = INVALID_ERROR_MESSAGE

    def get_id(self):
        return self.__command_id

    def set_id(self, command_id):
        self.__command_id = command_id

    def get_error_message(self):
        return self.__error_message

    def set_error_message(self, error_message):
        self.__error_message = error_message

    def is_error(self):
        return self.__error_message

    def set_no_error(self):
        self.__error_message = ""

    def is_valid(self):
        return all([self.__command_id != INVALID_COMMAND_ID,
                    self.__error_message != INVALID_ERROR_MESSAGE])

    def print_output(self):
        pass


class RobotCommandExecutor:
    def execute(self, robot_command_request):
        robot_command_response = self._create_response()
        robot_command_response.set_id(robot_command_request.get_id())
        self.__set_error_message(robot_command_response, robot_command_request)
        return robot_command_response

    @staticmethod
    def __set_error_message(robot_command_response, robot_command_request):
        if not robot_command_request.is_valid():
            robot_command_request.set_error_message("Invalid request.")
        else:
            robot_command_response.set_no_error()

    def _create_response(self):
        raise NotImplementedError()


class PlaceCommandRequest(RobotCommandRequest):
    def __init__(self):
        super().__init__()
        self.__position = Point()
        self.__orientation = Orientation.INVALID

    def get_position(self):
        return self.__position

    def set_position(self, point):
        self.__position = point

    def get_orientation(self):
        return self.__orientation

    def set_orientation(self, orientation):
        self.__orientation = orientation

    def is_valid(self):
        return all([super().is_valid(),
                   self.__position.is_valid(),
                   self.__orientation.is_valid()])


class PlaceCommandResponse(RobotCommandResponse):
    def __init__(self):
        super().__init__()


class PlaceCommandExecutor(RobotCommandExecutor):
    def execute(self, request):
        response = super().execute(request)
        if not response.is_error():
            PlaceCommandExecutor.__execute_place(request, response)
        return response

    @staticmethod
    def __execute_place(request, response):
        if world_model.get_board().is_valid_position(request.get_position()):
            robot = world_model.get_robot()
            robot.set_position(request.get_position())
            robot.set_orientation(request.get_orientation())
        else:
            response.set_error_message("Invalid position.")

    def _create_response(self):
        return PlaceCommandResponse()


class ReportCommandRequest(RobotCommandRequest):
    def __init__(self):
        super().__init__()


class ReportCommandResponse(RobotCommandResponse):
    def __init__(self):
        super().__init__()
        self.__position = Point()
        self.__orientation = Orientation.INVALID

    def get_position(self):
        return self.__position

    def set_position(self, point):
        self.__position = point

    def get_orientation(self):
        return self.__orientation

    def set_orientation(self, orientation):
        self.__orientation = orientation

    def is_valid(self):
        return all([super().is_valid(),
                    self.__position.is_valid(),
                    self.__orientation.is_valid()])

    def print_output(self):
        if self.is_valid():
            print(f"{self.__position.get_x():d},{self.__position.get_y():d},{self.__orientation.name:s}")
        else:
            print("not in place")


class ReportCommandExecutor(RobotCommandExecutor):
    def execute(self, request):
        response = super().execute(request)
        if not response.is_error():
            self.__execute_report(response)
        return response

    @staticmethod
    def __execute_report(response):
        robot = world_model.get_robot()
        response.set_position(robot.get_position())
        response.set_orientation(robot.get_orientation())

    def _create_response(self):
        return ReportCommandResponse()


class MobileRobot:
    def __init__(self):
        self.__position = Point()
        self.__orientation = Orientation.INVALID

    def get_position(self):
        return self.__position

    def set_position(self, point):
        self.__position = point

    def get_orientation(self):
        return self.__orientation

    def set_orientation(self, orientation):
        self.__orientation = orientation


class Board:
    MIN_POSITION = Point(0, 0)
    MAX_POSITION = Point(4, 4)

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


class InterpreterCommandEntry:
    def __init__(self, request_class, executor_class, custom_request_setter):
        self.request_class = request_class
        self.executor_class = executor_class
        self.custom_request_setter = custom_request_setter


def place_setter(arguments, place_request):
    if len(arguments) == 3:
        place_request.set_position(Point(int(arguments[0]), int(arguments[1])))
        place_request.set_orientation(Orientation[arguments[2]])


def report_setter(arguments, report_request):
    pass


class Interpreter:
    command_token_to_request = {
        'PLACE': InterpreterCommandEntry(PlaceCommandRequest, PlaceCommandExecutor, place_setter),
        'REPORT': InterpreterCommandEntry(ReportCommandRequest, ReportCommandExecutor, report_setter)
    }

    def __init__(self):
        self.__next_command_id = 0

    def execute_line(self, line):
        command_name, arguments = Interpreter.__extract_command(line)
        interpreter_command_entry = self.command_token_to_request.get(command_name, None)
        if interpreter_command_entry:
            request = self.__create_command_request(interpreter_command_entry, arguments)
            return self.__execute_command_request(interpreter_command_entry, request)
        return None

    @staticmethod
    def __extract_command(line):
        command_name = ''
        arguments = []
        tokens = line.replace(",", " ").split(" ")
        if tokens:
            command_name = tokens[0]
            arguments = tokens[1:]
        return command_name, arguments

    def __create_command_request(self, interpreter_command_entry, arguments):
        request = interpreter_command_entry.request_class()
        request.set_id(self.__get_next_command_id())
        interpreter_command_entry.custom_request_setter(arguments, request)
        return request

    @staticmethod
    def __execute_command_request(interpreter_command_entry, request):
        executor = interpreter_command_entry.executor_class()
        return executor.execute(request)

    def __get_next_command_id(self):
        current_id = self.__next_command_id
        self.__next_command_id += 1
        return current_id


world_model = WorldModel()


def main():
    interpreter = Interpreter()
    for line in sys.stdin:
        response = interpreter.execute_line(line.strip())
        if response:
            response.print_output()


if __name__ == "__main__":
    main()
