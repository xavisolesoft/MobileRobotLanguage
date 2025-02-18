import App.RobotCommand.Command as RobotCommand
import App.RightCommand.Command as RightCommand


class CommandExecutor(RobotCommand.Executor):
    def __init__(self, world_model):
        self.__world_model = world_model

    def execute(self, request):
        response = super().execute(request)
        if not response.is_error():
            self.__execute_move()
        return response

    def __execute_move(self):
        robot = self.__world_model.get_robot()
        next_orientation = robot.get_orientation().get_right_rotated()
        robot.set_orientation(next_orientation)

    def _create_response(self):
        return RightCommand.Response()
