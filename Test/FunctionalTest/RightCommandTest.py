import unittest
import sys
import os.path

sys.path.extend([os.path.dirname(os.path.abspath(__file__)) + "/../.."])
import Definitions
sys.path.extend([Definitions.APP_PATH])

import Test.FunctionalTest.Util as Util


class RightCommandTestCase(unittest.TestCase):
    def test_right_not_in_place(self):
        program = 'RIGHT\n' \
                  'REPORT\n'

        expected_output = 'not in place\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_right_success(self):
        program = 'PLACE 1,2,NORTH\n' \
                  'RIGHT\n' \
                  'REPORT\n' \
                  'RIGHT\n' \
                  'REPORT\n' \
                  'RIGHT\n' \
                  'REPORT\n' \
                  'RIGHT\n' \
                  'REPORT\n'

        expected_output = '1,2,EAST\n' \
                          '1,2,SOUTH\n' \
                          '1,2,WEST\n' \
                          '1,2,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
