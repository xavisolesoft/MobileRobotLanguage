import sys
import App.RobotLanguage as RobotLanguage
import App.RobotModel as RobotModel


def main():
    world_model = RobotModel.WorldModel()
    command_register = RobotLanguage.CommandRegister()
    command_controller = RobotLanguage.CommandController(world_model)
    interpreter = RobotLanguage.Interpreter(command_register, command_controller)
    for line in sys.stdin:
        output_message = interpreter.execute_line(line.strip())
        if output_message:
            print(output_message)


if __name__ == "__main__":
    main()
