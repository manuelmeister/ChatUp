import socket

HOST, PORT = "localhost", 12345

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = ""
name = input("Username eingeben: ")
sock.connect((HOST, PORT))
sock.sendall(bytes(name, "utf-8"))

while (data != "exit"):
    data = input("Ich:")
    try:
        # Connect to server and send data
        sock.sendall(bytes(data, "utf-8"))
    except:
        sock.close()