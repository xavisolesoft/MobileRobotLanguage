class Register:
    def __init__(self):
        self.command_name_to_definition = {}

    def get_command_definition(self, command_name):
        return self.command_name_to_definition.get(command_name, None)

    def set_command_definition(self, command_name, command_definition):
        self.command_name_to_definition[command_name] = command_definition


class Definition:
    def __init__(self,
                 request_class,
                 executor_class,
                 custom_interpreter_arguments_request_setter,
                 command_output_generator):
        self.request_class = request_class
        self.executor_class = executor_class
        self.custom_interpreter_arguments_request_setter = custom_interpreter_arguments_request_setter
        self.command_output_generator = command_output_generator
