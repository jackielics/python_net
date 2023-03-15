#!/usr/bin/env python3
#coding:utf-8
#代码4-5 s socket05s.py
import socket
import psutil
def do_cpu():
    data=str(psutil.cpu_percent(0))+'n' # 参数为0秒表示取得CPU的瞬间利用率
    count=0 # 记录已经取得信息的进程数量
    for process in psutil.process_iter():
        data=data+process.name()
        data=data+','+str(process.pid)
        cpu_usage_rate_process=str(process.cpu_percent(0))+'%'
        data=data+','+cpu_usage_rate_process+'\n'
        count +=1
        if count==10:
            break
    return data
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.157.130',8090))
print('Bind UDP on 8090...')
while True:
    (info,addr)=s.recvfrom(1024) # 从socket.sendto发送过来的
    data=do_cpu()
    s.sendto(data.encode('utf-8'),addr) # socket直接向指定的地址和端口号发送数据（与conn不同
    print('The client is ', addr)
    print('Sended CPU data is:', data)