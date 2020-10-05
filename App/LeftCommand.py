import App.RobotCommand.Command as Command
import App.RobotCommand.Register as CommandRegister


class CommandRequest(Command.Request):
    def __init__(self):
        super().__init__()


class CommandResponse(Command.Response):
    def __init__(self):
        super().__init__()


class CommandExecutor(Command.Executor):
    def __init__(self, world_model):
        self.__world_model = world_model

    def execute(self, request):
        response = super().execute(request)
        if not response.is_error():
            self.__execute_left()
        return response

    def __execute_left(self):
        robot = self.__world_model.get_robot()
        next_orientation = robot.get_orientation().get_left_rotated()
        robot.set_orientation(next_orientation)

    def _create_response(self):
        return CommandResponse()


def set_request_arguments_from_input_interpreter_arguments(arguments, place_request):
    pass


def command_interpreter_output_generator(response):
    pass


def get_command_definition():
    return \
        CommandRegister.CommandDefinition(CommandRequest,
                                          CommandExecutor,
                                          set_request_arguments_from_input_interpreter_arguments,
                                          command_interpreter_output_generator)
