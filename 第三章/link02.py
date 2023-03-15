#代码3-21ink02.py #!/usr/bin/env python3#coding:utf-8
import psutil
info=psutil.net_if_addrs()
print('info =', info)
print('type(info)=', type(info))
net1 = info['WLAN'] # 网卡
print('net1=', net1)
print('type(net1)=', type(net1))
packet = net1[0]
print('packet =', packet)
print('type(packet)=', type(packet))
print('mac_addr =', packet.address)

# import psutil
# if_stats = psutil.net_if_stats()
# for interface in if_stats:
#     if if_stats[interface].isup:
#         print(f"Interface {interface} is up")
