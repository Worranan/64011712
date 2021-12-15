import socket
import random

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.61"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
    def first():
        numcolor = []
        buttons = {}
        for i in range(0, 9):

            numcolor.append([])

            for j in range(0, 9):
                buttons[str(i)+ " " + str(j)] = (i,j)
                n = random.randint(0,3)
                numcolor[i].append(n)
        return numcolor,buttons
        # print(self.numcolor)

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)