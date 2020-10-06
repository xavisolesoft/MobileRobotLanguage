def set_request_arguments_from_input_interpreter_arguments(arguments, report_request):
    pass


def command_interpreter_output_generator(response):
    if response.is_valid():
        return str(response.get_position().get_x()) + "," + \
              str(response.get_position().get_y()) + "," + \
              str(response.get_orientation().name)
    else:
        return "not in place"
