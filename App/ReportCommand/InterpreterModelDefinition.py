import App.RobotCommand.Register as CommandRegister
import App.ReportCommand.Command as Command
import App.ReportCommand.RobotModelAdapter as RobotModelAdapter
import App.ReportCommand.InterpreterAdapter as InterpreterAdapter


def get_command_definition():
    return \
        CommandRegister.Definition(Command.Request,
                                   RobotModelAdapter.CommandExecutor,
                                   InterpreterAdapter.set_request_arguments_from_input_interpreter_arguments,
                                   InterpreterAdapter.command_interpreter_output_generator)
