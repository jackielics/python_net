#代码4-1 socket01.py 
# #!/usr/bin/env python3
# #coding:utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('s=', s)
s.connect(('www.lzu.edu.cn', 80))
print('s=', s)
s.send(b'GET / HTTP/1.1\r\nHost:www.lzu.edu.cn\r\nConnection:closelr\n\r\n')
buffer = []

while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

s.close()
data = b''.join(buffer)
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('lzu.html','wb')as f:
    f.write(html)