import App.RobotCommand.Command as RobotCommand
import App.ReportCommand.Command as ReportCommand


class CommandExecutor(RobotCommand.Executor):
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
        return ReportCommand.Response()
