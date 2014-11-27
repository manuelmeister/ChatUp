import socket, threading, sys, time

class Sender:
    def __init__(self):
        self.name = input("Name: ")
        self.host = 'localhost'
        self.port = 12345
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect((self.host, self.port))
        self.sock.sendall(bytes(self.name, "utf-8"))
        print("sender online")


    def send_data(self, sock, data):

        if data=="end" or data=="break" or data=="exit":
            exit()
        self.sock.sendall(bytes(data + "\n", "utf-8"))

