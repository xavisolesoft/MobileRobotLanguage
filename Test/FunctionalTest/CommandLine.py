import unittest
import subprocess


def run_interactive_app(input_program):
    p = subprocess.run(['python', '../../App/main.py'], stdout=subprocess.PIPE,
                       input=input_program, encoding='ascii')
    return p.stdout


class MyTestCase(unittest.TestCase):
    def test_report(self):
        program = 'REPORT\n'

        expected_output = 'not in place\n'

        output = run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_ignores_commands_before_report(self):
        program = 'MOVE\n' \
                  'LEFT\n' \
                  'RIGHT\n' \
                  'REPORT\n'

        expected_output = 'not in place\n'

        output = run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_place(self):
        program = 'PLACE 1,2,NORTH\n' \
                  'REPORT\n'

        expected_output = '1,2,NORTH\n'

        output = run_interactive_app(program)
        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
