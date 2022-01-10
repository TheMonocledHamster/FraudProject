import os
import subprocess

relpath = lambda p: os.path.normpath(os.path.join(os.path.dirname(__file__), p))

subprocess.call(relpath("python DBSetup/InitializeTables.py"), shell=True)
subprocess.call(relpath("python DBSetup/PopulateTables.py"), shell=True)
subprocess.call(relpath("python DBSetup/AddFkeys.py"), shell=True)