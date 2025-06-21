# socket is an internal endpoint for sending and recieving data

# socket is like an outlet that give connection from grid to transformer to house

# network socket allows you to send and recieve dat because it works locally

# socket library - impliment sockets with different protocols;

# socket module - import to use then call in socket function

# create object then object calls socket function

# socket family - afi net (socket.soc) used to specificy protocol used for communication either IPv4 or IPv6

# socet type - socket stream - specifies connection oriented protocols like TCP(three way handshake)
# UDP uses soc degram

# common methods
# bind
# listen
# accept
# send
# recieve

import socket

# creates socket object
serversocket = socket.socket(
    # socket family
    socket.AF_INET, 
    
    # socket type
    socket.SOCK_STREAM
)

# store hostname
host = socket.gethostbyname()

# port
port = 444

# bind host and port to object createdd
# binds host and port address to a socket
serversocket.bind(host, port)

# ca specify amount of requests at a time
serversocket.listen(3)

while True:
    # establish connection
    clientsocket, address = serversocket.accept()

    print("Recieve connection from " % str(address))

    message = "Thank you for connecting to a servere." + "\r\n"

    clientsocket.close()