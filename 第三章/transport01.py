#代码3-5 transport01.py
#!/usr/bin/env python3#coding:utf-8
import psutil
info = psutil.net_io_counters()
print('info=', info)
print('type(info)=', type(info))
print('bytes_sent =', info.bytes_sent)
print('bytes_recv =', info.bytes_recv)
print('packets_sent =', info.packets_sent)
print('packets_recv =', info.packets_recv)
print('errin =', info.errin)
print('errout=', info.errout)
print('dropin=', info.dropin)
print('dropout =', info.dropout)

