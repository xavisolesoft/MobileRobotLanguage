import subprocess
import App.Definitions


def run_interactive_app(input_program):
    p = subprocess.run(['python', App.Definitions.APP_PATH + '/main.py'], stdout=subprocess.PIPE,
                       input=input_program, encoding='ascii')
    return p.stdout
