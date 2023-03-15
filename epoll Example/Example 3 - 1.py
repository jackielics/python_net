import socket
import select
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(1)
serversocket.setblocking(0) # use non-blocking (asynchronous) mode
epoll = select.epoll() # create an epoll object
epoll.register(serversocket.fileno(), select.EPOLLIN) # Register interest in read events on the server socket. 
try:
    connections = {}
    requests = {}
    responses = {}
    while True:
        events = epoll.poll(1) # Query the epoll object to find out if any events of interest may have occurred. 
        for fileno, event in events: # fileno is a synonym for file descriptor and is always an integer.
            if fileno == serversocket.fileno(): # If a read event occurred on the socket server, then a new socket connection may have been created.
                connection, address = serversocket.accept()
                connection.setblocking(0)
                epoll.register(connection.fileno(), select.EPOLLIN) # Register interest in read (EPOLLIN) events for the new socket.
                connections[connection.fileno()] = connection
                requests[connection.fileno()] = b''
                responses[connection.fileno()] = response
            elif event & select.EPOLLIN: 
                # If a read event occurred on the socket, then the socket is ready to receive data.
                requests[fileno] += connections[fileno].recv(1024) # Read data from the socket.
                if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                    epoll.modify(fileno, select.EPOLLOUT) # Register interest in write (EPOLLOUT) events for the socket.
                    print('-'*40 + '\n' + requests[fileno].decode()[:-2])
            elif event & select.EPOLLOUT: 
                # If a write event occurred on the socket, then the socket is ready to send data.
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                if len(responses[fileno]) == 0:
                    epoll.modify(fileno, 0)
                    connections[fileno].shutdown(socket.SHUT_RDWR)
            elif event & select.EPOLLHUP: # If a hang-up event occurred on the socket, then the client has closed the connection.
                epoll.unregister(fileno) # Unregister interest in this socket connection.
                connections[fileno].close()
                del connections[fileno]
finally:
    """     Open socket connections don't need to be closed 
    since Python will close them when the program terminates. 
    They're included as a matter of good form. """
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()
