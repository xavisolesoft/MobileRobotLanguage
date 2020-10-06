import unittest
import Test.FunctionalTest.Util as Util


class PlaceCommandTestCase(unittest.TestCase):
    def test_one_place(self):
        program = 'PLACE 1,2,NORTH\n' \
                  'REPORT\n'

        expected_output = '1,2,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_two_place_same_place(self):
        program = 'PLACE 1,2,NORTH\n' \
                  'REPORT\n' \
                  'PLACE 1,2,NORTH\n' \
                  'REPORT\n'

        expected_output = '1,2,NORTH\n' \
                          '1,2,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_two_place_different_place(self):
        program = 'PLACE 1,2,NORTH\n' \
                  'REPORT\n' \
                  'PLACE 3,4,SOUTH\n' \
                  'REPORT\n'

        expected_output = '1,2,NORTH\n' \
                          '3,4,SOUTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_one_place_onside_board_and_one_place_outside_board(self):
        program = 'PLACE 1,2,NORTH\n' \
                  'REPORT\n' \
                  'PLACE 7,7,SOUTH\n' \
                  'REPORT\n'

        expected_output = '1,2,NORTH\n' \
                          '1,2,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_one_place_outside_board_top(self):
        program = 'PLACE 1,5,NORTH\n' \
                  'REPORT\n'

        expected_output = 'not in place\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_one_place_outside_board_bottom(self):
        program = 'PLACE 1,-1,NORTH\n' \
                  'REPORT\n'

        expected_output = 'not in place\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_one_place_outside_board_left(self):
        program = 'PLACE -1,1,NORTH\n' \
                  'REPORT\n'

        expected_output = 'not in place\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_one_place_outside_board_right(self):
        program = 'PLACE 5,1,NORTH\n' \
                  'REPORT\n'

        expected_output = 'not in place\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_one_place_with_inner_spaces(self):
        program = '    PLACE    1,   1,    NORTH    \n' \
                  '  REPORT \n'

        expected_output = '1,1,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
