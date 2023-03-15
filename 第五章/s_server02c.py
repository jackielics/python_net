#代码5-8 c s server02c.py 
#!/usr/bin/env python3
#coding:utf-8
import socket 
ip = '192.168.157.130'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
xx_s=input('Enter a number:')
xx_b=xx_s.encode('utf-8')
s.sendto(xx_b,(ip,8988))
while True:
    (result_b,s_addr) = s.recvfrom(1024)
    if s_addr[0]==ip:
        result_s=result_b.decode('utf-8')
        print('Factorial(%s)=%s'%(xx_s,result_s))
        break
s.close()