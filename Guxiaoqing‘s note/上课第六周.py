import IPy
import socket


#判断ip地址和网段是否包含于另一个网段中
print('192.168.1.100' in IPy.IP('192.168.1.0/24'))
print(IPy.IP('192.168.1.0/24') in IPy.IP('192.168.0.0/16'))

#判断俩个网段是否存在重叠，采用IPy提供的overlaps方法
print(IPy.IP('192.168.0.0/24').overlaps('192.168.1.0/24'))
print(IPy.IP('192.168.1.0/24').overlaps('192.168.2.0/24'))

#使用IPy中的IPSet方法汇总不连续的IP网段
IP=IPy.IPSet([IPy.IP('192.168.1.0/30'),IPy.IP('192.168.1.0/24')])
print(IP)


# 接收用户输入，参数为IP地址或网段地址
ip_s = input('请输入IP地址或者网段地址：')
ips = IPy.IP(ip_s)
if len(ips) > 1:  # 若输入为一个网络地址
    print('网络地址： %s' % ips.net())
    print('网络掩码地址： %s' % ips.netmask())
    print('网络广播地址： %s' % ips.broadcast())
    print('网络子网数： %s' % len(ips))
else:  # 若输入为单个IP地址
    print('IP反向解析： %s' % ips.reverseNames()[0])

print('十六进制地址： %s' % ips.strHex())
print('二进制地址： %s' % ips.strBin())
print('地址类型： %s' % ips.iptype())
