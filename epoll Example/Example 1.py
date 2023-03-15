# Example 1 is a simple Python server that listens on port 8080 for an HTTP request message, 
# prints it to the console, and sends an HTTP response message back to the client.

import socket
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
# Permits the bind() in line 11 even if another program was recently listening on the same port.
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 重用对应地址和端口
serversocket.bind(('0.0.0.0', 8080))  # 绑定地址和端口
serversocket.listen(1)  # 监听
connectiontoclient, address = serversocket.accept()  # 接受连接
request = b''
while EOL1 not in request and EOL2 not in request:  # 读取请求
    request += connectiontoclient.recv(1024)
print(request.decode())
connectiontoclient.send(response)
connectiontoclient.close()
serversocket.close()
