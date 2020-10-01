import sys
import App.RobotLanguage as RobotLanguage


def main():
    interpreter = RobotLanguage.Interpreter()
    for line in sys.stdin:
        output_message = interpreter.execute_line(line.strip())
        if output_message:
            print(output_message)


if __name__ == "__main__":
    main()
