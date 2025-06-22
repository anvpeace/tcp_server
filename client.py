import socket


# creates socket and specifiec protocol version 
clientsocket = socket.socket(
    socket.AF_INET, 
    socket.SOCK_STREAM
)

# server ip
# specify every time or make sure client knows ip
host = socket.gethostname()

port = 444

clientsocket.connect((host, port))

# mage how data is being sent 
# max data allowed through port
message = clientsocket.recv(1024)

# message needs to be decoded since encoded on 'ascii'

clientsocket.close()

print(message.decode('ascii'))

