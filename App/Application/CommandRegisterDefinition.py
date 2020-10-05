import App.PlaceCommand.InterpreterModelDefinition as PlaceCommandDefinition
import App.ReportCommand.InterpreterModelDefinition as ReportCommandDefinition
import App.MoveCommand.InterpreterModelDefinition as MoveCommandDefinition
import App.LeftCommand.InterpreterModelDefinition as LeftCommandDefinition
import App.RightCommand.InterpreterModelDefinition as RightCommandDefinition


def init_command_register(command_register):
    command_register.set_command_definition('PLACE', PlaceCommandDefinition.get_command_definition())
    command_register.set_command_definition('REPORT', ReportCommandDefinition.get_command_definition())
    command_register.set_command_definition('MOVE', MoveCommandDefinition.get_command_definition())
    command_register.set_command_definition('LEFT', LeftCommandDefinition.get_command_definition())
    command_register.set_command_definition('RIGHT', RightCommandDefinition.get_command_definition())
