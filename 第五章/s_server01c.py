#代码5-7 cs server01c.py 
#!/usr/bin/env python3
#coding:utf-8
import socket 
ip = '192.168.157.130'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,8899))
xx_s = input('Enter a number:')
xx_b = xx_s.encode('utf-8')
s.send(xx_b)
result_b = s.recv(1024)
results = result_b.decode('utf-8')
print('Factorial(%s)=%s'%(xx_s, results))
s.close()