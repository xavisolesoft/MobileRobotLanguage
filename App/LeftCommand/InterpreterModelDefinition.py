import App.RobotCommand.Register as CommandRegister
import App.LeftCommand.Command as Command
import App.LeftCommand.RobotModelAdapter as RobotModelAdapter
import App.LeftCommand.InterpreterAdapter as InterpreterAdapter


def get_command_definition():
    return \
        CommandRegister.CommandDefinition(Command.Request,
                                          RobotModelAdapter.CommandExecutor,
                                          InterpreterAdapter.set_request_arguments_from_input_interpreter_arguments,
                                          InterpreterAdapter.command_interpreter_output_generator)
