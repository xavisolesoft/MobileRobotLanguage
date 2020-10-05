import App.RobotLanguage as RobotLanguage
import App.RobotModel as RobotModel
import App.RobotCommand.Register as CommandRegister
import App.RobotCommand.Control as CommandControl
import App.PlaceCommand as PlaceCommand
import App.ReportCommand as ReportCommand
import App.MoveCommand.InterpreterModelDefinition as MoveCommandDefinition
import App.LeftCommand.InterpreterModelDefinition as LeftCommandDefinition
import App.RightCommand as RightCommand


class SystemController:
    def __init__(self):
        self.__world_model = RobotModel.WorldModel()
        self.__command_register = CommandRegister.CommandRegister()
        self.__command_controller = CommandControl.CommandController(self.__world_model)
        self.__interpreter = RobotLanguage.Interpreter(self.__command_register, self.__command_controller)
        self.__init_command_register(self.__command_register)

    def execute_in_commands(self, input_file, output_file):
        for line in input_file:
            output_message = self.__interpreter.execute_line(line.strip())
            if output_message:
                output_file.write_line(output_message)

    @staticmethod
    def __init_command_register(command_register):
        command_register.set_command_definition('PLACE', PlaceCommand.get_command_definition())
        command_register.set_command_definition('REPORT', ReportCommand.get_command_definition())
        command_register.set_command_definition('MOVE', MoveCommandDefinition.get_command_definition())
        command_register.set_command_definition('LEFT', LeftCommandDefinition.get_command_definition())
        command_register.set_command_definition('RIGHT', RightCommand.get_command_definition())
