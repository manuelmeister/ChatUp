import socket
import sys

HOST, PORT = "172.16.2.118", 12345

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = ""

while (data != "exit"):
    data = input("Ich:")
    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))
    except:
        sock.close()