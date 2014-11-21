import socket

HOST = '172.16.2.133'    # The remote host
PORT = 12345              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
inputstring = input("Bitte Nachricht eingeben")
s.sendall(inputstring.encode("utf-8"))
data = s.recv(1024)
s.close()
print('Received', repr(data))