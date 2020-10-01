import sys
from enum import Enum
import App.RobotCommand as RobotCommand


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


class PlaceCommandRequest(RobotCommand.Request):
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


class PlaceCommandResponse(RobotCommand.Response):
    def __init__(self):
        super().__init__()


class PlaceCommandExecutor(RobotCommand.Executor):
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


class ReportCommandRequest(RobotCommand.Request):
    def __init__(self):
        super().__init__()


class ReportCommandResponse(RobotCommand.Response):
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


class ReportCommandExecutor(RobotCommand.Executor):
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


class CommandDefinition:
    def __init__(self, request_class, executor_class, custom_request_setter, command_output_generator):
        self.request_class = request_class
        self.executor_class = executor_class
        self.custom_request_setter = custom_request_setter
        self.command_output_generator = command_output_generator


def place_command_setter(arguments, place_request):
    if len(arguments) == 3:
        place_request.set_position(Point(int(arguments[0]), int(arguments[1])))
        place_request.set_orientation(Orientation[arguments[2]])


def report_command_setter(arguments, report_request):
    pass


def place_command_print(response):
    pass


def report_command_print(response):
    if response.is_valid():
        print(f"{response.get_position().get_x():d},"
              f"{response.get_position().get_y():d},"
              f"{response.get_orientation().name:s}")
    else:
        print("not in place")


class CommandRegister:
    def __init__(self):
        self.command_name_to_definition = {}
        self.set_command_definition('PLACE', CommandDefinition(PlaceCommandRequest, PlaceCommandExecutor, place_command_setter, place_command_print))
        self.set_command_definition('REPORT', CommandDefinition(ReportCommandRequest, ReportCommandExecutor, report_command_setter, report_command_print))

    def get_command_definition(self, command_name):
        return self.command_name_to_definition.get(command_name, None)

    def set_command_definition(self, command_name, command_definition):
        self.command_name_to_definition[command_name] = command_definition


class Interpreter:
    def __init__(self):
        self.__next_command_id = 0
        self.command_register = CommandRegister()

    def execute_line(self, line):
        command_name, arguments = Interpreter.__extract_command(line)
        command_definition = self.command_register.get_command_definition(command_name)
        if command_definition:
            return self.__execute_command(command_definition, arguments)
        return ""

    @staticmethod
    def __extract_command(line):
        command_name = ''
        arguments = []
        tokens = line.replace(",", " ").split(" ")
        if tokens:
            command_name = tokens[0]
            arguments = tokens[1:]
        return command_name, arguments

    def __execute_command(self, command_definition, arguments):
        request = self.__create_command_request(command_definition, arguments)
        response = self.__execute_command_request(command_definition, request)
        return command_definition.command_output_generator(response)

    def __create_command_request(self, command_definition, arguments):
        request = command_definition.request_class()
        request.set_id(self.__get_next_command_id())
        command_definition.custom_request_setter(arguments, request)
        return request

    @staticmethod
    def __execute_command_request(command_definition, request):
        executor = command_definition.executor_class()
        return executor.execute(request)

    def __get_next_command_id(self):
        current_id = self.__next_command_id
        self.__next_command_id += 1
        return current_id


world_model = WorldModel()


def main():
    interpreter = Interpreter()
    for line in sys.stdin:
        output_message = interpreter.execute_line(line.strip())
        if output_message:
            print(output_message)


if __name__ == "__main__":
    main()
