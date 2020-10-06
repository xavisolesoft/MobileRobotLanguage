import sys


class Interpreter:
    def __init__(self, command_register, command_controller):
        self.command_register = command_register
        self.command_controller = command_controller

    def execute_line(self, line):
        command_name, arguments = Interpreter.__extract_command(line)
        message = self.__execute_robot_command(command_name, arguments)
        message += self.__execute_interpreter_command(command_name, arguments)
        return message

    @staticmethod
    def __extract_command(line):
        tokens = line.replace(",", " ").split(" ")
        tokens = Interpreter.__remove_string_list_spaces(tokens)
        command_name, arguments = Interpreter.__split_tokens_by_command_arguments(tokens)
        return command_name, arguments

    @staticmethod
    def __remove_string_list_spaces(string_list):
        return list(filter(lambda a: a != "", string_list))

    @staticmethod
    def __split_tokens_by_command_arguments(tokens):
        command_name = ''
        arguments = []
        if tokens:
            command_name = tokens[0]
            arguments = tokens[1:]
        return command_name, arguments

    def __execute_robot_command(self, command_name, arguments):
        command_definition = self.command_register.get_command_definition(command_name)
        if command_definition:
            return self.command_controller.execute_command(command_definition, arguments)
        return ""

    @staticmethod
    def __execute_interpreter_command(command_name, arguments):
        if command_name == "EXIT":
            sys.exit()
        return ""
