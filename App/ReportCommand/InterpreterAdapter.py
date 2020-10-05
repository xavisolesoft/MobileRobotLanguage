def set_request_arguments_from_input_interpreter_arguments(arguments, report_request):
    pass


def command_interpreter_output_generator(response):
    if response.is_valid():
        print(f"{response.get_position().get_x():d},"
              f"{response.get_position().get_y():d},"
              f"{response.get_orientation().name:s}")
    else:
        print("not in place")
