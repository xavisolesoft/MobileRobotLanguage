import App.RobotCommand.Command as RobotCommand
import App.PlaceCommand.Command as PlaceCommand


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
        return PlaceCommand.Response()
