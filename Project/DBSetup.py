import os
import subprocess

relpath = lambda p: os.path.normpath(os.path.join(os.path.dirname(__file__), p))

subprocess.call(relpath("DBSetup/InitializeTables.py"), shell=True)
subprocess.call(relpath("DBSetup/PopulateTables.py"), shell=True)
subprocess.call(relpath("DBSetup/AddFkeys.py"), shell=True)
subprocess.call(relpath("DBSetup/NewPlanHandling.py"), shell=True)