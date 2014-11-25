import socket, threading, sys

class ChatClient:
    def __init__(self, gui, port=12345, host="localhost"): #!!!!!
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.users = {}

        self.gui = gui

        try:
            self.sock.connect((self.host,self.port))
        except socket.error:
            print("Failed to bind socket ",socket.error)
            sys.exit()

        self.run()


    def exit(self):
        self.sock.close()

    def listener(self):
        data = False
        while(not data):
            data = self.sock.recv(1024)
            self.gui.writeline(data.decode("utf-8"))

    def speaker(self):
        data = True
        while (data != "exit"):
            data = input("Ich:")
            try:
                # Connect to server and send data
                self.sock.sendall(bytes(data, "utf-8"))
            except:
                self.sock.close()
        self.sock.close()


    def run(self):
        self.gui.writeline("Waiting for connections on port" + self.port)
        name = "manuel"
        self.sock.sendall(bytes(name, "utf-8"))
        threading.Thread(target=self.listener,name='thread-listener').start()
