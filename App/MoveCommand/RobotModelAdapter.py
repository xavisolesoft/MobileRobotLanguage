import App.RobotCommand.Command as RobotCommand
import App.MoveCommand.Command as MoveCommand


class CommandExecutor(RobotCommand.Executor):
    def __init__(self, world_model):
        self.__world_model = world_model

    def execute(self, request):
        response = super().execute(request)
        if not response.is_error():
            self.__execute_move(response)
        return response

    def __execute_move(self, response):
        robot = self.__world_model.get_robot()
        next_position = robot.get_position() + robot.get_orientation().to_normalized_vector()
        if self.__world_model.get_board().is_valid_position(next_position):
            robot.set_position(next_position)
        else:
            response.set_error_message("Invalid position.")

    def _create_response(self):
        return MoveCommand.Response()
