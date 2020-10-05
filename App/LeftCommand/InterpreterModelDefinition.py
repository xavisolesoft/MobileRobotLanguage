import App.RobotCommand.Register as CommandRegister
import App.LeftCommand.Command as Command
import App.LeftCommand.RobotModelAdapter as RobotModelAdapter
import App.LeftCommand.InterpreterAdapter as InterpreterAdapter


def get_command_definition():
    definition = CommandRegister.Definition()
    definition.set_request_class(Command.Request)
    definition.set_executor_class(RobotModelAdapter.CommandExecutor)
    definition.set_command_output_generator(InterpreterAdapter.set_request_arguments_from_input_interpreter_arguments)
    definition.set_custom_interpreter_arguments_request_setter(InterpreterAdapter.command_interpreter_output_generator)
    return definition
