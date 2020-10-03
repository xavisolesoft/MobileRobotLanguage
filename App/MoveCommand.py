import App.RobotCommand as RobotCommand
import App.RobotModel as RobotModel


class CommandRequest(RobotCommand.Request):
    def __init__(self):
        super().__init__()


class CommandResponse(RobotCommand.Response):
    def __init__(self):
        super().__init__()


class CommandExecutor(RobotCommand.Executor):
    def __init__(self, world_model):
        self.__world_model = world_model

    def execute(self, request):
        response = super().execute(request)
        if not response.is_error():
            self.__execute_move(request, response)
        return response

    def __execute_move(self, request, response):
        robot = self.__world_model.get_robot()
        next_position = robot.get_position() + robot.get_orientation().to_normalized_vector()
        if self.__world_model.get_board().is_valid_position(next_position):
            robot.set_position(next_position)
        else:
            response.set_error_message("Invalid position.")

    def _create_response(self):
        return CommandResponse()


def set_request_arguments_from_input_interpreter_arguments(arguments, place_request):
    pass


def command_interpreter_output_generator(response):
    pass


def get_command_definition():
    return \
        RobotCommand.CommandDefinition(CommandRequest,
                                       CommandExecutor,
                                       set_request_arguments_from_input_interpreter_arguments,
                                       command_interpreter_output_generator)
