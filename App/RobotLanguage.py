import App.PlaceCommand as PlaceCommand
import App.ReportCommand as ReportCommand
import App.MoveCommand as MoveCommand
import App.LeftCommand as LeftCommand
import App.RightCommand as RightCommand


class CommandRegister:
    def __init__(self):
        self.command_name_to_definition = {}
        self.set_command_definition('PLACE', PlaceCommand.get_command_definition())
        self.set_command_definition('REPORT', ReportCommand.get_command_definition())
        self.set_command_definition('MOVE', MoveCommand.get_command_definition())
        self.set_command_definition('LEFT', LeftCommand.get_command_definition())
        self.set_command_definition('RIGHT', RightCommand.get_command_definition())

    def get_command_definition(self, command_name):
        return self.command_name_to_definition.get(command_name, None)

    def set_command_definition(self, command_name, command_definition):
        self.command_name_to_definition[command_name] = command_definition


class CommandController:
    def __init__(self, world_model):
        self.world_model = world_model
        self.__next_command_id = 0

    def execute_command(self, command_definition, arguments):
        request = self.__create_command_request(command_definition, arguments)
        response = self.__execute_command_request(command_definition, request)
        return command_definition.command_output_generator(response)

    def __create_command_request(self, command_definition, arguments):
        request = command_definition.request_class()
        request.set_id(self.__get_next_command_id())
        command_definition.custom_interpreter_arguments_request_setter(arguments, request)
        return request

    def __execute_command_request(self, command_definition, request):
        executor = command_definition.executor_class(self.world_model)
        return executor.execute(request)

    def __get_next_command_id(self):
        current_id = self.__next_command_id
        self.__next_command_id += 1
        return current_id


class Interpreter:
    def __init__(self, command_register, command_controller):
        self.command_register = command_register
        self.command_controller = command_controller

    def execute_line(self, line):
        command_name, arguments = Interpreter.__extract_command(line)
        command_definition = self.command_register.get_command_definition(command_name)
        if command_definition:
            return self.command_controller.execute_command(command_definition, arguments)
        return ""

    @staticmethod
    def __extract_command(line):
        command_name = ''
        arguments = []
        tokens = line.replace(",", " ").split(" ")
        if tokens:
            command_name = tokens[0]
            arguments = tokens[1:]
        return command_name, arguments
