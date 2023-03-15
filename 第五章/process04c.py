#!/usr/bin/env python3
#coding:utf-8
#代码5-4c process04c.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_addr = ('192.168.157.130', 8095)
s.sendto(b'CPU', s_addr)
(data_b, addr) = s.recvfrom(1024)
data_s = data_b.decode('utf-8')
if addr == s_addr:
  data_s = data_b.decode('utf-8')
  data_list = data_s.split('\n')
  print('CPU usage rate is ', data_list[0])
  print('Top 10 processes are flowing...')
  print('%-20s%-5s%-10s' % ('NAME', 'PID', 'CPU usage'))
  data_list = data_list[1:-1]
  for xx in data_list:
    yy = xx.split(',')
    print('%-20s%-5s%-10s' % (yy[0], yy[1], yy[2]))

s.close()