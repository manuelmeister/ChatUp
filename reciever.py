import socket, threading, sys, time

class Reciever:
    def __init__(self):
        print("reciever online")

    def recieve_data(self):
        # data = False
        # while(not data):
        #     data = self.sock.recv(1024)
        # return data

        while True:
            host = 'localhost'
            port = 12345
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, port))
            s.listen(1)
            conn, addr = s.accept()
            print('\rConnected by', addr[0], "\nIch : ", end="")
            while True:
                data = conn.recv(1024)
                if not data:
                    print("Connection to", addr[0],"closed\n")
                    conn.close()
                    break
                print('\rReceived by', addr[0], ";", "timestamp:", time.asctime(time.localtime(time.time())), "\n", data.decode("utf-8"), "\nIch : ", end="")
            conn.close()



