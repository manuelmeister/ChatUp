import socket, threading, sys

class ChatServer:
    def __init__(self, port=12345, host="localhost"):
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.users = {}
        self.threads = []

        try:
            self.sock.bind((self.host,self.port))
        except socket.error:
            print("Failed to bind socket ",socket.error)
            sys.exit()

        self.sock.listen(10)
        self.run()

    def exit(self):
        self.sock.close()

    def threadrunner(self,client,addr):
        name = self.users[client]
        print("Client",name,"connected with ",addr[0],":",str(addr[1]))
        while True:
            data = client.recv(1024)
            if not data:
                del self.users[client]
                break
            print(name.decode("utf-8"),":", data.decode("utf-8"))
            for user in self.users:
                if user == client:
                    return
                else:
                    user.sendall(name + b":" + data)

        client.close()

    def run(self):
        print("Waiting for connections on port",self.port)
        while True:
            client, addr = self.sock.accept()
            name = client.recv(1024)

            self.users[client] = name.decode("utf-8")

            threading.Thread(target=self.threadrunner, args=(client,addr)).start()