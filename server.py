# Tcp Chat server
import socket


while True:

    HOST = ''
    PORT = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("Connection to", addr, "closed")
            break
        print('Received', data.decode("utf-8"))
        conn.sendall(data)
    conn.close()