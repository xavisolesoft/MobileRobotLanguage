# Mobile Robot Language
Implementation for a mobile robot language simulator using Model-View-Controller architecture with command pattern, functional testing for all the system and unit testing of the more stable parts. 

- The application is a command line interactive application.
- The map is a 5x5 board without obstacles.
- The robot is not able to move outside the map (movement instruction with target outside the map will have no effect).

## Architecture explanation

The architecture is a decoupled Model-View-Controller to be able to implement more Views in the future or implement a new simulator_model/real_robot_model. Each command is implemented in a different module to be able to add new commands without modify other modules.

### Modules

- **RobotLanguage:** Contains the interpreter for the robot language and implements the generic part for the View.
- **RobotModel:** Contains the implementation of the Model.
- **RobotCommand:** Contains the generic part for the Controller implementation.
- **[CommandName]Command:** Implementation for the specific part for each command.
  - **Command:** Part of the Controller for this module independent from View and Model (Request and Response for the command controller).
  - **InterpreterAdapter:** Transform functions from:
    - Interpreter input (command argument string list) to command request.
    - Command response to interpreter output (interpreter command output message).
  - **RobotModelAdapter:** Implementation for the execution of the Controller, coupled to the Model and the Controller.
  - **InterpreterModelDefinition:** Definition of all the functions and classes that need to be registered for a command.
- **Application:** Controls the system execution; defines the commands and their implementation; and allocates all the sub parts of the system.
- **Geometry:** Library for geometry representation and geometry operations.

## Language description

### Commands

```
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
EXIT
```

- `PLACE` will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.
- The origin (0,0) can be considered to be the SOUTH WEST most corner.
- The first valid command to the robot is a `PLACE` command, after that, any sequence of commands may be issued, in any order, including another `PLACE` command. The application should discard all commands in the sequence until a valid `PLACE` command has been executed
- `MOVE` will move the toy robot one unit forward in the direction it is currently facing.
- `LEFT` and `RIGHT` will rotate the robot 90 degrees in the specified direction without changing the position of the robot.
- `REPORT` will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient.
- `EXIT` end the command line program.
- A robot that is not on the table can choose to ignore the `MOVE`, `LEFT`, `RIGHT` and `REPORT` commands.
- Input can be from a file, or from standard input, as the developer chooses.
- Provide test data to exercise the application.

### Constraints

- The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot.
- Any move that would cause the robot to fall must be ignored.

### How to run the application

```
cd MobileRobotLaguage
python App/main.py
```

### How to run a functional test

```
cd MobileRobotLaguage
python Test/FunctionalTest/<Test_file_name>.py
```

### How to run a unit test

```
cd MobileRobotLaguage
python Test/UnitTest/<Test_file_name>.py
```

### Example Input and Output:

#### Example a

```
PLACE 0,0,NORTH
MOVE
REPORT
```

Expected output:

```
0,1,NORTH
```

#### Example b

```
PLACE 0,0,NORTH
LEFT
REPORT
```

Expected output:

```
0,0,WEST
```

#### Example c

```
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
```

Expected output

```
3,3,NORTH
```

### Python version

Python 3.6