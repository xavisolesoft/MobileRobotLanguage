import App.RobotLanguage as RobotLanguage
import App.RobotModel as RobotModel
import App.RobotCommand.Register as CommandRegister
import App.Application.CommandRegisterDefinition as CommandRegisterDefinition
import App.RobotCommand.Control as CommandControl


class Controller:
    def __init__(self):
        self.__world_model = RobotModel.WorldModel()
        self.__command_register = CommandRegister.Register()
        CommandRegisterDefinition.init_command_register(self.__command_register)
        self.__command_controller = CommandControl.CommandController(self.__world_model)
        self.__interpreter = RobotLanguage.Interpreter(self.__command_register, self.__command_controller)

    def execute_in_commands(self, input_file, output_file):
        for line in input_file:
            output_message = self.__interpreter.execute_line(line.strip())
            if output_message:
                output_file.write_line(output_message)