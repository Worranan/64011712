import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5555))
s.listen(5)
while True:
    msg = "Hello you can connect server"
    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been estabilsh!")
        clientsocket.send(bytes(msg, "utf-8"))
        while True:
            a = input("Enter 2 ")
            msg = f"The time is {a}"
            print(msg)

            clientsocket.send(bytes(msg,"utf-8"))


# msg = input("Enter : ")
# print(f'{len(msg):<10}' + msg)
