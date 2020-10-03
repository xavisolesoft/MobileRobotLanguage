import App.RobotLanguage as RobotLanguage
import App.RobotModel as RobotModel


class SystemController:
    def __init__(self):
        self.__world_model = RobotModel.WorldModel()
        self.__command_register = RobotLanguage.CommandRegister()
        self.__command_controller = RobotLanguage.CommandController(self.__world_model)
        self.__interpreter = RobotLanguage.Interpreter(self.__command_register, self.__command_controller)

    def execute_in_commands(self, input_file, output_file):
        for line in input_file:
            output_message = self.__interpreter.execute_line(line.strip())
            if output_message:
                output_file.write_line(output_message)