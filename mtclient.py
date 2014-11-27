import socket



# Create a socket (SOCK_STREAM means a TCP socket)


host = 'localhost'
port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect((host, port))
data = ""
name = input("Username eingeben: ")
sock.sendall(bytes(name, "utf-8"))




while (data != "exit"):
    data = input("Ich:")
    try:
        # Connect to server and send data
        sock.sendall(bytes(data, "utf-8"))
    except:
        sock.close()