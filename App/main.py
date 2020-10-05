import sys

import App.Application.System as System


def main():
    system_controller = System.Controller()
    system_controller.execute_in_commands(sys.stdin, sys.stdout)


if __name__ == "__main__":
    main()
