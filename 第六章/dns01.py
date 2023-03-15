# 代码6-7#!/usr/bin/env python3
# coding:utf-8
import dns.resolver
# from dns import resolver


def resolver(domain, type):
    rt_obj = dns.resolver.query(domain, type)
    ans_list = rt_obj.response.answer
    print('Type %s records are:' % type)
    for xx in ans_list:
        print(xx.to_text())


resolver('www.baidu.com', 'A') # 用于将域名转换成IP地址。
resolver('baidu.com', 'MX') # 用于定位邮件地址中的域名所对应的服务器
resolver('baidu.com', 'NS') # 标记区域的域名服务器及授权子域
resolver('www.baidu.com', 'CNAME') # 别名记录，用于域名间的映射
resolver('baidu.com', 'SOA') # 用于标记区域的起始授权点
