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
