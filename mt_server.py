import socket, threading, sys

class ChatServer:
    def __init__(self, port=12345, host=''):
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}
        self.threads = []

        try:
            self.sock.bind((self.host,self.port))
        except socket.error:
            print("Failed to bind socket ",socket.error)
            sys.exit()

        self.sock.listen(10)

    def exit(self):
        self.sock.close()

    def threadrunner(self,client,addr):
        name = self.clients[client]
        print("Client",name,"connected with ",addr[0],":",str(addr[1]))
        while True:
            data = client.recv(1024)
            if not data:
                break
            print(name,":", data.decode("utf-8"))
            client.sendall(data)

        client.close()

    def run(self):
        print("Waiting for connections on port",self.port)
        while True:
            client, addr = self.sock.accept()
            name = client.recv(1024).decode("utf-8")

            self.clients[client] = name

            threading.Thread(target=self.threadrunner, args=(client,addr)).start()

if __name__ == "__main__":
    server = ChatServer()
    server.run()