import sys
import App.RobotCommand as RobotCommand
import App.Geometry as Geometry
import App.RobotModel as RobotModel


class PlaceCommandRequest(RobotCommand.Request):
    def __init__(self):
        super().__init__()
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
        if RobotModel.world_model.get_board().is_valid_position(request.get_position()):
            robot = RobotModel.world_model.get_robot()
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
        robot = RobotModel.world_model.get_robot()
        response.set_position(robot.get_position())
        response.set_orientation(robot.get_orientation())

    def _create_response(self):
        return ReportCommandResponse()


class CommandDefinition:
    def __init__(self, request_class, executor_class, custom_request_setter, command_output_generator):
        self.request_class = request_class
        self.executor_class = executor_class
        self.custom_request_setter = custom_request_setter
        self.command_output_generator = command_output_generator


def place_command_setter(arguments, place_request):
    if len(arguments) == 3:
        place_request.set_position(Geometry.Point(int(arguments[0]), int(arguments[1])))
        place_request.set_orientation(Geometry.Orientation[arguments[2]])


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


def main():
    interpreter = Interpreter()
    for line in sys.stdin:
        output_message = interpreter.execute_line(line.strip())
        if output_message:
            print(output_message)


if __name__ == "__main__":
    main()
