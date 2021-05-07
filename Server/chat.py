import socket
import threading

# parameters = ipv4 & tcp(for UDP, use "DGRAM")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding our socket to an address and a port
sock.bind(('0.0.0.0', 10000))

sock.listen(1)

connections = []

def handler(c, a):
    global connections
    # handling a connection by recieving data from that connection
    while True:

        # Max 1024 bytes
        data = c.recv(1024)

        # sending data back to every user connected
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connections.remove(c)
            c.close()
            break

# loop to handle the connections
while True:
    c, a = sock.accept()

    # we need a new thread everytime there's a new connection
    # parameters = name of the function that runs when we run the thread, 
    cThread = threading.Thread(target=handler, args=(c,a))

    # set this to 'True' for closing the program regardless of running threads
    cThread.daemon = True
    cThread.start()
    connections.append(c)
    print(connections)
