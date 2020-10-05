import App.RobotCommand.Register as CommandRegister
import App.RightCommand.Command as Command
import App.RightCommand.RobotModelAdapter as RobotModelAdapter
import App.RightCommand.InterpreterAdapter as InterpreterAdapter


def get_command_definition():
    return \
        CommandRegister.Definition(Command.Request,
                                   RobotModelAdapter.CommandExecutor,
                                   InterpreterAdapter.set_request_arguments_from_input_interpreter_arguments,
                                   InterpreterAdapter.command_interpreter_output_generator)
