class Register:
    def __init__(self):
        self.command_name_to_definition = {}

    def get_command_definition(self, command_name):
        return self.command_name_to_definition.get(command_name, None)

    def set_command_definition(self, command_name, command_definition):
        self.command_name_to_definition[command_name] = command_definition


class Definition:
    def __init__(self):
        self.__request_class = None
        self.__executor_class = None
        self.__custom_interpreter_arguments_request_setter = None
        self.__command_output_generator = None

    def set_request_class(self, instantiable):
        self.__request_class = instantiable

    def get_request_class(self):
        return self.__request_class

    def set_executor_class(self, instantiable):
        self.__executor_class = instantiable

    def get_executor_class(self):
        return self.__executor_class

    def set_custom_interpreter_arguments_request_setter(self, callable_object):
        self.__custom_interpreter_arguments_request_setter = callable_object

    def get_custom_interpreter_arguments_request_setter(self):
        return self.__custom_interpreter_arguments_request_setter

    def set_command_output_generator(self, callable_object):
        self.__command_output_generator = callable_object

    def get_command_output_generator(self):
        return self.__command_output_generator
