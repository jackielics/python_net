#!/usr/bin/env python3
# coding:utf-8
# 代码6-6 ftp01.py

from ftplib import FTP
import os


def ftp_connect(host, username, password):
    '''连接和登录FTP服务器'''
    ftp = FTP()
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp


def ftp_download(ftp, remotefile, localfile):
    '''从FTP服务器下载文件'''
    f = open(localfile, 'wb')
    ftp.retrbinary('RETR ' + remotefile, f.write)  # 从FTP服务器下载文件（记得空格）
    f.close()


def ftp_upload(ftp, remotefile, localfile):
    '''上传文件到FTP服务器'''
    f = open(localfile, 'rb')
    ftp.storbinary('STOR ' + remotefile, f)  # 上传文件到FTP服务器（记得空格）
    f.close()


ftp = ftp_connect("192.168.157.130", "jack", "123")  # 连接和登录FTP服务器
print(ftp.getwelcome())
file_list = ftp.nlst()  # 取得服务器当前工作目录的内容
print(file_list)
ftp_download(ftp, "a.txt", "./a.txt")
ftp_download(ftp, "b.txt", "./b.txt")
ftp_upload(ftp, "myls", "./myls")
file_list = ftp.nlst()
print(file_list)
ftp.quit()
