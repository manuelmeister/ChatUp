import socket, threading, sys

class ChatServer:
    def __init__(self, user,port=12345, host=''):
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}
        self.threads = []

        try:
            self.server.bind((self.host,self.port))
        except socket.error:
            print("Failed to bind socket ",socket.error)
            sys.exit()

        self.server.listen(10)

    def exit(self):
        self.server.close()

    def threadrunner(self,client,addr):
        print("Client connected with ",addr[0],":",str(addr[1]))
        while True:
            name = self.clients[client]
            data = client.recv(1024)
            if not data:
                break
            print(data.decode("utf-8"))
            client.sendall(data)

        client.close()

    def run(self):
        print("Waiting for connections on port",self.port)
        while True:
            client, addr = self.server.accept()
            name = client.recv(1024)

            self.clients[client] = name

            threading.Thread(target=self.threadrunner, args=(client,addr)).start()

if __name__ == "__main__":
    server = ChatServer()
    server.run()