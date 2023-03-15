#代码3-4 network02.py
#!/usr/bin/env python3#coding:utf-8
import netifaces
info=netifaces.gateways()
print('info=',info)
print('type(info)=',type(info))
gateway_addr=info['default'][2][0]
print('gateway_addr =', gateway_addr)