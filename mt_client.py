import socket, threading, sys, time

class ChatClient:
    port = int()
    host = ""
    sock = socket.socket()
    # port = port
    # host = host
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # users = {}

    def __init__(self):
        port = 12345
        host = "localhost"
        self.port = port
        self.host = host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.users = {}

        try:
            self.sock.connect((self.host,self.port))
        except socket.error:
            print("Failed to bind socket ",socket.error)
            sys.exit()

        self.run()


    def exit(self):
        self.sock.close()

    def listen(self):
        data = False
        while(not data):
            data = self.sock.recv(1024)
        return data


    def speak(self, message):
        try:       # Connect to server and send data
            self.sock.sendall(bytes(message, "utf-8"))
        except:
            self.sock.close()
            print("Failed to send")
        self.sock.close()


    def run(self):
        name = "manuel"
        self.sock.sendall(bytes(name, "utf-8"))
        #threading.Thread(target=self.listener,name='thread-listener').start()
