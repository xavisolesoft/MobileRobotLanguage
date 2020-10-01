import App.RobotCommand as RobotCommand
import App.Geometry as Geometry
import App.RobotModel as RobotModel


class CommandRequest(RobotCommand.Request):
    def __init__(self):
        super().__init__()


class CommandResponse(RobotCommand.Response):
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


class CommandExecutor(RobotCommand.Executor):
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
        return CommandResponse()


def command_setter(arguments, report_request):
    pass


def command_print(response):
    if response.is_valid():
        print(f"{response.get_position().get_x():d},"
              f"{response.get_position().get_y():d},"
              f"{response.get_orientation().name:s}")
    else:
        print("not in place")


def get_command_definition():
    return \
        RobotCommand.CommandDefinition(CommandRequest,
                                       CommandExecutor,
                                       command_setter,
                                       command_print)
