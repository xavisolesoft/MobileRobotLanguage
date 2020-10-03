import sys

import App.Application as Application


def main():
    system_controller = Application.SystemController()
    system_controller.execute_in_commands(sys.stdin, sys.stdout)


if __name__ == "__main__":
    main()
