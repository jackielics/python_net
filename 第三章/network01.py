#代码3-3 network01.py !/usr/bin/env python3#coding:utf-8
import psutil
info = psutil.net_if_addrs()
# print('info =', info)
net1 = info['WLAN']
# net2 = info['lo']
# print('net1 =', net1)
# print('net2 ', net2)
print('net1[0]=', net1[0])
print('net1[1]=', net1[1])
print('IPv4_addr =', net1[1].address)
print('IPv6_addr =', net1[0].address)

print(__import__('psutil').net_if_addrs()['WLAN'][1].address)
