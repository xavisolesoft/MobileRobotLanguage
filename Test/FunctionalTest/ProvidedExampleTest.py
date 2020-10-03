import unittest
import Test.FunctionalTest.Util as Util


class MyTestCase(unittest.TestCase):
    def test_example_a(self):
        program = 'PLACE 0,0,NORTH\n' \
                  'MOVE\n' \
                  'REPORT\n'

        expected_output = '0,1,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_example_b(self):
        program = 'PLACE 0,0,NORTH\n' \
                  'LEFT\n' \
                  'REPORT\n'

        expected_output = '0,0,WEST\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)

    def test_example_c(self):
        program = 'PLACE 1,2,EAST\n' \
                  'MOVE\n'\
                  'MOVE\n' \
                  'LEFT\n' \
                  'MOVE\n' \
                  'REPORT\n'

        expected_output = '3,3,NORTH\n'

        output = Util.run_interactive_app(program)
        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
