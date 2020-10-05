import App.RobotCommand.Command as Command
import App.RobotCommand.Register as CommandRegister
import App.Geometry as Geometry


class CommandRequest(Command.Request):
    def __init__(self):
        super().__init__()


class CommandResponse(Command.Response):
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


class CommandExecutor(Command.Executor):
    def __init__(self, world_model):
        self.__world_model = world_model

    def execute(self, request):
        response = super().execute(request)
        if not response.is_error():
            self.__execute_report(response)
        return response

    def __execute_report(self, response):
        robot = self.__world_model.get_robot()
        response.set_position(robot.get_position())
        response.set_orientation(robot.get_orientation())

    def _create_response(self):
        return CommandResponse()


def set_request_arguments_from_input_interpreter_arguments(arguments, report_request):
    pass


def command_interpreter_output_generator(response):
    if response.is_valid():
        print(f"{response.get_position().get_x():d},"
              f"{response.get_position().get_y():d},"
              f"{response.get_orientation().name:s}")
    else:
        print("not in place")


def get_command_definition():
    return \
        CommandRegister.CommandDefinition(CommandRequest,
                                          CommandExecutor,
                                          set_request_arguments_from_input_interpreter_arguments,
                                          command_interpreter_output_generator)
