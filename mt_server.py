import socket, threading, sys

class ChatServer:
    def __init__(self, port=12345, host=''):
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}

        try:
            self.server.bind((self.host,self.port))
        except socket.error:
            print("Failed to bind socket ",socket.error)
            sys.exit()

        self.server.listen(10)

    def exit(self):
        self.server.close()

    def threadrunner(self,conn,addr):
        print("Client connected with ",addr[0],":",str(addr[1]))
        while True:
            data = conn.recv(1024)
            if not data: break
            #param = data.split('.')
            #if param[0] == "@name":
            #    return
            reply = b"OK..." + data
            print(reply.decode("utf-8"))
            conn.sendall(reply)

        conn.close()

    def run(self):
        print("Waiting for connections on port",self.port)
        while True:
            conn, addr = self.server.accept()
            threading.Thread(target=self.threadrunner, args=(conn,addr)).start()

if __name__ == "__main__":
    server = ChatServer()
    server.run()