""" Example 2 adds a loop in line 15 to repeatedly processes client connections until 
interrupted by the user (e.g. with a keyboard interrupt). This illustrates more clearly 
that the server socket is never used to exchange data with the client. Rather, it accepts 
a connection from a client, and then creates a new socket on the server machine that is 
used to communicate with the client. """
# blocking sockets
import socket
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(1)
try:
    while True:
        connectiontoclient, address = serversocket.accept()
        request = b''
        while EOL1 not in request and EOL2 not in request:
            request += connectiontoclient.recv(1024)
        print('-'*40 + '\n' + request.decode()[:-2])
        connectiontoclient.send(response)
        connectiontoclient.close()
finally:
    serversocket.close()
