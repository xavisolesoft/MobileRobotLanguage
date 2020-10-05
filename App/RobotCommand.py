INVALID_COMMAND_ID = -1


class Request:
    def __init__(self):
        self.__command_id = INVALID_COMMAND_ID

    def get_id(self):
        return self.__command_id

    def set_id(self, command_id):
        self.__command_id = command_id

    def is_valid(self):
        return self.__command_id != INVALID_COMMAND_ID


class Response:
    INVALID_ERROR_MESSAGE = "INVALID ERROR MESSAGE"

    def __init__(self):
        self.__command_id = INVALID_COMMAND_ID
        self.__error_message = self.INVALID_ERROR_MESSAGE

    def get_id(self):
        return self.__command_id

    def set_id(self, command_id):
        self.__command_id = command_id

    def get_error_message(self):
        return self.__error_message

    def set_error_message(self, error_message):
        self.__error_message = error_message

    def is_error(self):
        return self.__error_message

    def set_no_error(self):
        self.__error_message = ""

    def is_valid(self):
        return all([self.__command_id != INVALID_COMMAND_ID,
                    self.__error_message != self.INVALID_ERROR_MESSAGE])


class Executor:
    def execute(self, robot_command_request):
        robot_command_response = self._create_response()
        robot_command_response.set_id(robot_command_request.get_id())
        self.__set_error_message(robot_command_response, robot_command_request)
        return robot_command_response

    @staticmethod
    def __set_error_message(robot_command_response, robot_command_request):
        if not robot_command_request.is_valid():
            robot_command_request.set_error_message("Invalid request.")
        else:
            robot_command_response.set_no_error()

    def _create_response(self):
        raise NotImplementedError()


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


class CommandRegister:
    def __init__(self):
        self.command_name_to_definition = {}

    def get_command_definition(self, command_name):
        return self.command_name_to_definition.get(command_name, None)

    def set_command_definition(self, command_name, command_definition):
        self.command_name_to_definition[command_name] = command_definition


class CommandDefinition:
    def __init__(self, request_class, executor_class, custom_interpreter_arguments_request_setter, command_output_generator):
        self.request_class = request_class
        self.executor_class = executor_class
        self.custom_interpreter_arguments_request_setter = custom_interpreter_arguments_request_setter
        self.command_output_generator = command_output_generator
