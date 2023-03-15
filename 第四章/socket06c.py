#代码4-6 c socket06c.py
#!/usr/bin/env python3
#coding:utf-8
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_addr=('192.168.157.130',8091)
s.bind(('192.168.68.133',8888)) # 客户端本机的地址和端口
s.sendto(b'memory info',s_addr)
(data_b,addr)=s.recvfrom(1024)
if addr==s_addr:
    data_s=data_b.decode('utf-8')
    print('Memory status is flowing...')
    data_list = data_s.split(',')
    for xx in data_list:
        print(xx)
s.close()