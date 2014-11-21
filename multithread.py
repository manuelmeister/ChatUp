import socket, threading

def connect():
    address = ''
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((address, port))
    s.listen(1) 
    print("Server started! Waiting for connections...")
    while True:
        accept_connection(s)

def accept_connection(s):
    connection, address = s.accept()
    print('Client connected with address:', address)
    t = threading.Thread(target=message, args=[connection])
    t.start()

def message(connection):
    try:
        while 1:
            data = connection.recv(1024)
            if not data: break
            #connection.sendall(b'-- Message Received --\n')
            print(data.decode('utf-8'))
    except:
        connection.close()
        pass

connect()