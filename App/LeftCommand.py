import App.RobotCommand as RobotCommand
import App.RobotModel as RobotModel


class CommandRequest(RobotCommand.Request):
    def __init__(self):
        super().__init__()


class CommandResponse(RobotCommand.Response):
    def __init__(self):
        super().__init__()


class CommandExecutor(RobotCommand.Executor):
    def execute(self, request):
        response = super().execute(request)
        if not response.is_error():
            CommandExecutor.__execute_move(request, response)
        return response

    @staticmethod
    def __execute_move(request, response):
        robot = RobotModel.world_model.get_robot()
        next_orientation = robot.get_orientation().get_left_rotated()
        robot.set_orientation(next_orientation)

    def _create_response(self):
        return CommandResponse()


def command_setter(arguments, place_request):
    pass


def command_print(response):
    pass


def get_command_definition():
    return \
        RobotCommand.CommandDefinition(CommandRequest,
                                       CommandExecutor,
                                       command_setter,
                                       command_print)
