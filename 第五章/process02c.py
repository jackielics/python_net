#代码5-2c process02c
#!/usr/bin/env python3
#coding:utf-8
import socket, time, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.157.130',8088))
# filename='/bin/ls'
filename = input("File u want to get:")
print('I want to get the file %s!' % filename)
s.send(filename.encode('utf-8'))
str1 = s.recv(1024) # 先recv yes或者no
str2 = str1.decode('utf-8')
if str2=='no':
    print('To get the file $s is failed!' % filename)
else:
    s.send(b'I am ready!')
    temp = filename.split('/')
    myname = 'process02_' + temp[len(temp)-1]
    size = 1024
    with open(myname, 'wb') as f:
        # 以二进制打开
        while True:
            data = s.recv(size)
            f.write(data)
            file_descriptor = f.fileno()
            file_stat = os.fstat(file_descriptor)
            print("len(data)", len(data))
            print("file_stat.st_size", file_stat.st_size)
            time.sleep(0.1)
            if len(data) < size:
                break
    print('The downloaded file is %s.' % myname)
s.close()