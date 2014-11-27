import socket
from threading import Thread
from tkinter import *
import time


class Controller(object):
    def __init__(self, app):
        Thread.__init__(self)
        self.model = Model('localhost', 12345, "manuel")
        self.app = app
        self.view = View(self.app)

        self.view.cmdSubmit.bind_class("Button", "<Button-1>", self.onClick)

        tcpthread = Thread(name='tcp', target=self.startReceiving()).start()
        guithread = Thread(name='gui', target=self.startMainloop()).start()

    def onClick(self, event):
        self.model.send(self.view.txtInput.get())
        self.view.txtInput.delete(0, END)

    def startReceiving(self):
        data_received = True
        while data_received:
            data_received = self.model.receive()
            self.view.writeLine(data_received)
            time.sleep(0.1)

    def startMainloop(self):
        self.app.mainloop()


class View():
    def __init__(self, app):
        Thread.__init__(self)
        self.app = app
        self.app.title("ChatUp")

        self.txtChat = Text(self.app, height=20, width=50, bg="#bbbbbb")
        self.txtChat.pack(side=TOP)

        self.txtInput = Entry(self.app, width=50)
        self.txtInput.pack(side=LEFT)

        self.cmdSubmit = Button(self.app, width=10, text="Submit")
        self.cmdSubmit.pack(side=RIGHT)

    def writeLine(self, strMessage):
        self.txtChat.insert(END, strMessage + "\n")


class Model(object):
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = name

        self.connect()
        self.send(name)

    def connect(self):
        try:
            self.sock.bind((self.host, self.port))
            self.sock.listen(1)
            self.sock.connect()
        except:
            sys.exit()

    def receive(self):
        self.data = self.sock.recv(1024)
        if not self.data:
            self.sock.close()
            return False
        return self.data


    def send(self, content):
        self.sock.sendall(bytes(content, encoding='utf-8'))


if __name__ == "__main__":
    app = Tk()
    controller = Controller(app)