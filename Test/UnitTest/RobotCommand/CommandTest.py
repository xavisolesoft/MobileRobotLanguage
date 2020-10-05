import unittest
import App.RobotCommand.Command as Command


class RequestTestCase(unittest.TestCase):
    def test_constructor(self):
        request = Command.Request()

        self.assertEqual(Command.INVALID_COMMAND_ID, request.get_id())
        self.assertFalse(request.is_valid())

    def test_set_get_id(self):
        command_id = 5
        request = Command.Request()

        request.set_id(command_id)
        self.assertEqual(command_id, request.get_id())

    def test_is_valid_true(self):
        command_id = 5
        request = Command.Request()

        request.set_id(command_id)
        self.assertTrue(request.is_valid())

    def test_is_valid_false(self):
        command_id = Command.INVALID_COMMAND_ID
        request = Command.Request()

        request.set_id(command_id)
        self.assertFalse(request.is_valid())


class ResponseTestCase(unittest.TestCase):
    def test_constructor(self):
        response = Command.Response()

        self.assertEqual(Command.INVALID_COMMAND_ID, response.get_id())
        self.assertEqual(Command.Response.INVALID_ERROR_MESSAGE, response.get_error_message())
        self.assertFalse(response.is_valid())
        self.assertTrue(response.is_error())

    def test_set_get_id(self):
        command_id = 5
        response = Command.Response()

        response.set_id(command_id)
        self.assertEqual(command_id, response.get_id())

    def test_set_get_error_message(self):
        error_message = "error"
        response = Command.Response()

        response.set_error_message(error_message)
        self.assertEqual(error_message, response.get_error_message())

    def test_set_no_error_is_error(self):
        response = Command.Response()

        response.set_no_error()
        self.assertFalse(response.is_error())

    def test_is_error_set_error_message_true(self):
        error_message = "error"
        response = Command.Response()

        response.set_error_message(error_message)
        self.assertTrue(response.is_error())

    def test_is_error_false(self):
        error_message = ""
        response = Command.Response()

        response.set_error_message(error_message)
        self.assertFalse(response.is_error())

    def test_is_valid_true(self):
        command_id = 5
        response = Command.Response()

        response.set_id(command_id)
        self.assertFalse(response.is_valid())

    def test_is_valid_not_valid_id_and_error_message(self):
        command_id = Command.INVALID_COMMAND_ID
        error_message = Command.Response.INVALID_ERROR_MESSAGE
        response = Command.Response()

        response.set_id(command_id)
        response.set_error_message(error_message)
        self.assertFalse(response.is_valid())

    def test_is_valid_not_valid_id_and_is_error(self):
        command_id = Command.INVALID_COMMAND_ID
        error_message = "error"
        response = Command.Response()

        response.set_id(command_id)
        response.set_error_message(error_message)
        self.assertFalse(response.is_valid())

    def test_is_valid_not_valid_id_and_not_is_error(self):
        command_id = Command.INVALID_COMMAND_ID
        error_message = ""
        response = Command.Response()

        response.set_id(command_id)
        response.set_error_message(error_message)
        self.assertFalse(response.is_valid())

    def test_is_valid_not_valid_error_message(self):
        command_id = 50
        error_message = Command.Response.INVALID_ERROR_MESSAGE
        response = Command.Response()

        response.set_id(command_id)
        response.set_error_message(error_message)
        self.assertFalse(response.is_valid())


class RobotCommandExecutorTestCase(unittest.TestCase):
    class RobotCommandTestExecutor(Command.Executor):
        def _create_response(self):
            return Command.Response()

    def test_must_implement_create_response(self):
        executor = Command.Executor()
        request = Command.Request()
        self.assertRaises(NotImplementedError, executor.execute, request)

    def test_execute_correct_response_id(self):
        command_id = 7
        executor = self.RobotCommandTestExecutor()
        request = Command.Request()
        request.set_id(command_id)

        response = executor.execute(request)
        self.assertEqual(command_id, response.get_id())

    def test_execute_valid_request_return_no_error_response(self):
        executor = self.RobotCommandTestExecutor()
        request = Command.Request()

        response = executor.execute(request)
        self.assertFalse(response.is_valid())

    def test_execute_not_valid_request_return_error_response(self):
        executor = self.RobotCommandTestExecutor()
        request = Command.Request()

        response = executor.execute(request)
        self.assertEqual(Command.Response.INVALID_REQUEST_ERROR, response.get_error_message())


if __name__ == '__main__':
    unittest.main()
