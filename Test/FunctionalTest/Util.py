import sys
import os.path
import subprocess

sys.path.extend([os.path.dirname(os.path.abspath(__file__)) + "/.."])

sys.path.extend(["../.."])
import Definitions
sys.path.extend([Definitions.APP_PATH])


def run_interactive_app(input_program):
    p = subprocess.run(['python', Definitions.APP_PATH + '/main.py'], stdout=subprocess.PIPE,
                       input=input_program, encoding='ascii')
    return p.stdout
