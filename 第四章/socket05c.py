#!/usr/bin/env python3
#coding:utf-8
#代码4-5 c socket05c.py

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_addr=('192.168.157.130',8090)
s.sendto(b'CPU info',s_addr) # socket向服务器直接发送bytes类型的数据“CPU info”
(data_b,addr)=s.recvfrom(1024) # 接收服务器的回应信息
if addr ==s_addr:
    data_s=data_b.decode('utf-8')
    data_list = data_s.split('\n')
    print('CPU usage rate is',data_list[0])
    print('Top 10 processes are flowing...')
    print('%-20s%-5s%-10s'%('NAME','PID','CPU usage'))
    data_list=data_list[1:-1]
    for xx in data_list:
        yy = xx.split(',')
        print('%-20s%-5s%-10s'%(yy[0],yy[1],yy[2]))
s.close()