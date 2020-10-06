import unittest
import sys
import os.path

sys.path.extend([os.path.dirname(os.path.abspath(__file__)) + "/../.."])
import Definitions
sys.path.extend([Definitions.APP_PATH])

import Test.FunctionalTest.Util as Util


class ReportCommandTestCase(unittest.TestCase):
    def test_one_report(self):
        program = 'REPORT\n'

        expected_output = 'not in place\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_ignores_commands_before_report(self):
        program = 'MOVE\n' \
                  'LEFT\n' \
                  'RIGHT\n' \
                  'REPORT\n'

        expected_output = 'not in place\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
