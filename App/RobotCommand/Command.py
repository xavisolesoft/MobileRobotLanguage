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
