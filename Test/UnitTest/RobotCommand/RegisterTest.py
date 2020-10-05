import unittest
import App.RobotCommand.Register as Register


class DefinitionCase(unittest.TestCase):
    class TestClass:
        def __init__(self):
            a = 1

    @staticmethod
    def test_function():
        return 0

    def test_constructor(self):
        definition = Register.Definition()

        self.assertEqual(None, definition.get_request_class())
        self.assertEqual(None, definition.get_executor_class())
        self.assertEqual(None, definition.get_command_output_generator())
        self.assertEqual(None, definition.get_custom_interpreter_arguments_request_setter())

    def test_set_get_request_class(self):
        definition = Register.Definition()

        definition.set_request_class(self.TestClass)

        self.assertEqual(self.TestClass, definition.get_request_class())

    def test_set_get_executor_class(self):
        definition = Register.Definition()

        definition.set_executor_class(self.TestClass)

        self.assertEqual(self.TestClass, definition.get_executor_class())

    def test_set_get_command_output_generator(self):
        definition = Register.Definition()

        definition.set_command_output_generator(self.test_function)

        self.assertEqual(self.test_function, definition.get_command_output_generator())

    def test_set_get_custom_interpreter_arguments_request_setter(self):
        definition = Register.Definition()

        definition.set_custom_interpreter_arguments_request_setter(self.test_function)

        self.assertEqual(self.test_function, definition.get_custom_interpreter_arguments_request_setter())


class RegisterCase(unittest.TestCase):
    def test_set_get_definition(self):
        definition = Register.Definition()
        register = Register.Register()
        self.assertEqual(None, register.get_command_definition())

        register.set_command_definition("TEST", definition)

        self.assertEqual(definition, register.get_command_definition())


if __name__ == '__main__':
    unittest.main()
