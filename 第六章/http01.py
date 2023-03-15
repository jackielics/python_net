#代码6-1http01.py #!/usr/bin/env python3#coding:utf-8
import urllib.request
import json

code = '101160101'
url = 'http://www.weather.com.cn/data/cityinfo/%s.html' % code  # 不一定要加上括号
print('url=', url)
obj = urllib.request.urlopen(url)  # urlopen()打开给定的网址
print('type(obj)=', type(obj))
data_b = obj.read()  # )从对象obj中读取内容（bytes）
print('data b=', data_b)
data_s = data_b.decode('utf-8')  # 将字节串转换为字符串
print('data s=', data_s)
data_dict = json.loads(data_s)  # 将字符串转换为字典
print('data dict=', data_dict)
rt = data_dict['weatherinfo']
print('rt=', rt)
my_rt = ('%s,%s,%s~%s') % (rt['city'], rt['weather'], rt['temp1'], rt['temp2'])
print(my_rt)