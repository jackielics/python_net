#!/usr/bin/env python3
#coding:utf-8
#代码4-4 socket04.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5) # 该 socket 对象进行的所有 I/O 操作都会受到超时时间的影响
ip = '192.168.157.130'
for port in range(5000,9000):
    result = s.connect_ex((ip,port)) # 0.5s内没有成功连接即为失败
    if result == 0:
        print('port %d is openned!' % port)
s.close()