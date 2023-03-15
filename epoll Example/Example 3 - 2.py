#!/usr/bin/python3
#coding:utf-8
""" 实现了一个简单的Web服务器，可以响应客户端的HTTP请求并返回"Hello, world!"的文本内容。 """
import socket, select
# 导入socket和select模块

EOL1 = b'\n\n'  # 终止符1
EOL2 = b'\n\r\n'  # 终止符2
# 设置两种终止符，用于判断HTTP请求是否结束

response  = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
# HTTP响应头
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
# HTTP响应头的Content-Type和Content-Length字段
response += b'Hello, world!'
# HTTP响应内容

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 创建一个TCP套接字
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 设置套接字选项，允许地址重用
serversocket.bind(('0.0.0.0', 8080))
# 绑定服务器地址和端口号
serversocket.listen(1)
# 监听TCP连接请求
serversocket.setblocking(0)
# 设置套接字为非阻塞模式

epoll = select.epoll()
# 创建一个epoll对象
epoll.register(serversocket.fileno(), select.EPOLLIN)
# 将服务器套接字添加到epoll的关注列表中，关注事件为可读事件

try:
   connections = {}; requests = {}; responses = {}
   # 创建字典用于保存连接、请求和响应
   while True:
      events = epoll.poll(1)
      # 等待epoll事件，最多等待1秒
      for fileno, event in events:
         if fileno == serversocket.fileno():
            # 如果是服务器套接字上有事件，说明有新连接请求到来
            connection, address = serversocket.accept()
            # 接受新连接
            connection.setblocking(0)
            # 设置连接套接字为非阻塞模式
            epoll.register(connection.fileno(), select.EPOLLIN)
            # 将连接套接字添加到epoll的关注列表中，关注事件为可读事件
            connections[connection.fileno()] = connection
            requests[connection.fileno()] = b''
            # 初始化请求字典，将请求数据设置为空字节串
            responses[connection.fileno()] = response
            # 初始化响应字典，将响应数据设置为固定的HTTP响应内容
         elif event & select.EPOLLIN:
            # 如果是连接套接字上有可读事件
            requests[fileno] += connections[fileno].recv(1024)
            # 读取数据到请求字典中
            if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
               # 如果读取到了终止符
               epoll.modify(fileno, select.EPOLLOUT)
               # 修改关注事件为可写事件
               print('-'*40 + '\n' + requests[fileno].decode()[:-2])
               #  # 打印HTTP请求内容
         elif event & select.EPOLLOUT:
            # 如果是连接套接字上有可写事件
            byteswritten = connections[fileno].send(responses[fileno])
            # 发送响应数据到连接套接字中
            responses[fileno] = responses[fileno][byteswritten:]
            # 更新响应字典中的响应数据
            if len(responses[fileno]) == 0:
               # 如果响应数据全部发送完毕
               epoll.modify(fileno, 0)
               # 修改关注事件为0，即不关注任何事件
               connections[fileno].shutdown(socket.SHUT_RDWR)
               # 关闭连接套接字
         elif event & select.EPOLLHUP:
            # 如果连接套接字上出现挂起事件
            epoll.unregister(fileno)
            # 从epoll关注列表中删除连接套接字
            connections[fileno].close()
            # 关闭连接套接字
            del connections[fileno]
            # 从连接字典中删除连接套接字
           # 打印HTTP请求内容
         elif event & select.EPOLLOUT:
            # 如果是连接套接字上有可写事件
            byteswritten = connections[fileno].send(responses[fileno])
            # 发送响应数据到连接套接字中
            responses[fileno] = responses[fileno][byteswritten:]
            # 更新响应字典中的响应数据
            if len(responses[fileno]) == 0:
               # 如果响应数据全部发送完毕
               epoll.modify(fileno, 0)
               # 修改关注事件为0，即不关注任何事件
               connections[fileno].shutdown(socket.SHUT_RDWR)
               # 关闭连接套接字
         elif event & select.EPOLLHUP:
            # 如果连接套接字上出现挂起事件
            epoll.unregister(fileno)
            # 从epoll关注列表中删除连接套接字
            connections[fileno].close()
            # 关闭连接套接字
            del connections[fileno]
            # 从连接字典中删除连接套接字
finally:
   epoll.unregister(serversocket.fileno())
   # 从epoll关注列表中删除服务器套接字
   epoll.close()
   # 关闭epoll对象
   serversocket.close()
   # 关闭服务器套接字