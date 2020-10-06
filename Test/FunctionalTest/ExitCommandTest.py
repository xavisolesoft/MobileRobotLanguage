import unittest
import sys
import os.path

sys.path.extend([os.path.dirname(os.path.abspath(__file__)) + "/../.."])
import Definitions
sys.path.extend([Definitions.APP_PATH])

import Test.FunctionalTest.Util as Util


class ExitCommandTestCase(unittest.TestCase):
    def test_exit(self):
        program = 'EXIT\n'

        expected_output = ''

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
