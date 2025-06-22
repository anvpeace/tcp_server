import socket


# creates socket object
serversocket = socket.socket(
    # socket family
    socket.AF_INET, 
    
    # socket type
    socket.SOCK_STREAM
)

# store hostname
host = socket.gethostname()

# port
port = 444

# bind host and port to object createdd
# binds host and port address to a socket
serversocket.bind((host, port))

# ca specify amount of requests at a time
serversocket.listen(3)

while True:
    # establish connection
    clientsocket, address = serversocket.accept()

    address = str(address)

    print("Recieve connection from " + address)

    message = "Thank you for connecting to a servere." + "\r\n"

    clientsocket.send(message.encode('ascii'))
    clientsocket.close()