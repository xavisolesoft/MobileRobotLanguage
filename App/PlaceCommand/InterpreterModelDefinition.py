import App.RobotCommand.Register as CommandRegister
import App.PlaceCommand.Command as Command
import App.PlaceCommand.RobotModelAdapter as RobotModelAdapter
import App.PlaceCommand.InterpreterAdapter as InterpreterAdapter


def get_command_definition():
    return \
        CommandRegister.CommandDefinition(Command.Request,
                                          RobotModelAdapter.CommandExecutor,
                                          InterpreterAdapter.set_request_arguments_from_input_interpreter_arguments,
                                          InterpreterAdapter.command_interpreter_output_generator)
