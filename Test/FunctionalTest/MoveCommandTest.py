import unittest
import sys
import os.path

sys.path.extend([os.path.dirname(os.path.abspath(__file__)) + "/../.."])
import Definitions
sys.path.extend([Definitions.APP_PATH])

import Test.FunctionalTest.Util as Util


class MoveCommandTestCase(unittest.TestCase):
    def test_move_not_in_place(self):
        program = 'MOVE\n' \
                  'REPORT\n'

        expected_output = 'not in place\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_move_north_success(self):
        program = 'PLACE 1,2,NORTH\n' \
                  'MOVE\n' \
                  'REPORT\n'

        expected_output = '1,3,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_move_south_success(self):
        program = 'PLACE 1,2,SOUTH\n' \
                  'MOVE\n' \
                  'REPORT\n'

        expected_output = '1,1,SOUTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_move_east_success(self):
        program = 'PLACE 1,2,EAST\n' \
                  'MOVE\n' \
                  'REPORT\n'

        expected_output = '2,2,EAST\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_move_west_success(self):
        program = 'PLACE 1,2,WEST\n' \
                  'MOVE\n' \
                  'REPORT\n'

        expected_output = '0,2,WEST\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_move_north_out_of_board(self):
        program = 'PLACE 4,4,NORTH\n' \
                  'MOVE\n' \
                  'REPORT\n'

        expected_output = '4,4,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_move_south_out_of_board(self):
        program = 'PLACE 0,0,SOUTH\n' \
                  'MOVE\n' \
                  'REPORT\n'

        expected_output = '0,0,SOUTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_move_east_out_of_board(self):
        program = 'PLACE 4,4,EAST\n' \
                  'MOVE\n' \
                  'REPORT\n'

        expected_output = '4,4,EAST\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_move_west_out_of_board(self):
        program = 'PLACE 0,0,WEST\n' \
                  'MOVE\n' \
                  'REPORT\n'

        expected_output = '0,0,WEST\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
