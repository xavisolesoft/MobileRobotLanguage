import unittest
import Test.FunctionalTest.Util as Util


class MyTestCase(unittest.TestCase):
    def test_1(self):
        program = 'MOVE\n' \
                  'LEFT\n' \
                  'RIGHT\n' \
                  'REPORT\n'

        expected_output = 'not in place\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_2(self):
        program = 'PLACE 1,2,NORTH\n' \
                  'REPORT\n'

        expected_output = '1,2,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_3(self):
        program = 'PLACE 9,9,NORTH\n' \
                  'REPORT\n'

        expected_output = 'not in place\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_4(self):
        program = 'PLACE 1,1,NORTH\n' \
                  'RIGHT\n' \
                  'REPORT\n'\
                  'RIGHT\n' \
                  'REPORT\n' \
                  'RIGHT\n' \
                  'REPORT\n' \
                  'RIGHT\n' \
                  'REPORT\n'

        expected_output = '1,1,EAST\n' \
                          '1,1,SOUTH\n' \
                          '1,1,WEST\n' \
                          '1,1,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_5(self):
        program = 'PLACE 1,1,NORTH\n' \
                  'LEFT\n' \
                  'REPORT\n'\
                  'LEFT\n' \
                  'REPORT\n' \
                  'LEFT\n' \
                  'REPORT\n' \
                  'LEFT\n' \
                  'REPORT\n'

        expected_output = '1,1,WEST\n' \
                          '1,1,SOUTH\n' \
                          '1,1,EAST\n' \
                          '1,1,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_6(self):
        program = 'PLACE 1,1,NORTH\n' \
                  'MOVE\n' \
                  'RIGHT\n'\
                  'REPORT\n' \
                  'MOVE\n' \
                  'RIGHT\n' \
                  'REPORT\n' \
                  'MOVE\n' \
                  'RIGHT\n' \
                  'REPORT\n' \
                  'MOVE\n' \
                  'RIGHT\n' \
                  'REPORT\n'

        expected_output = '1,2,EAST\n' \
                          '2,2,SOUTH\n' \
                          '2,1,WEST\n' \
                          '1,1,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_7(self):
        program = 'PLACE 4,4,NORTH\n' \
                  'MOVE\n' \
                  'MOVE\n'\
                  'MOVE\n' \
                  'MOVE\n' \
                  'MOVE\n' \
                  'REPORT\n'

        expected_output = '4,4,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_8(self):
        program = 'AUTODESTRUCT\n' \
                  'TAKEOFF\n' \
                  'KILL\n' \
                  'REPORT\n'

        expected_output = 'not in place\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
