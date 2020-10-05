import App.Geometry as Geometry


def set_request_arguments_from_input_interpreter_arguments(arguments, place_request):
    if len(arguments) == 3:
        place_request.set_position(Geometry.Point(int(arguments[0]), int(arguments[1])))
        place_request.set_orientation(Geometry.Orientation[arguments[2]])


def command_interpreter_output_generator(response):
    pass
