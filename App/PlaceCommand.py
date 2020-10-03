import App.RobotCommand as RobotCommand
import App.Geometry as Geometry
import App.RobotModel as RobotModel


class CommandRequest(RobotCommand.Request):
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


class CommandResponse(RobotCommand.Response):
    def __init__(self):
        super().__init__()


class CommandExecutor(RobotCommand.Executor):
    def __init__(self, world_model):
        self.__world_model = world_model

    def execute(self, request):
        response = super().execute(request)
        if not response.is_error():
            self.__execute_place(request, response)
        return response

    def __execute_place(self, request, response):
        if self.__world_model.get_board().is_valid_position(request.get_position()):
            robot = self.__world_model.get_robot()
            robot.set_position(request.get_position())
            robot.set_orientation(request.get_orientation())
        else:
            response.set_error_message("Invalid position.")

    def _create_response(self):
        return CommandResponse()


def set_request_arguments_from_input_interpreter_arguments(arguments, place_request):
    if len(arguments) == 3:
        place_request.set_position(Geometry.Point(int(arguments[0]), int(arguments[1])))
        place_request.set_orientation(Geometry.Orientation[arguments[2]])


def command_interpreter_output_generator(response):
    pass


def get_command_definition():
    return \
        RobotCommand.CommandDefinition(CommandRequest,
                                       CommandExecutor,
                                       set_request_arguments_from_input_interpreter_arguments,
                                       command_interpreter_output_generator)
