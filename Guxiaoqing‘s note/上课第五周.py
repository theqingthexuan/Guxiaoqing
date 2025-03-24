import IPy

# 通过version获取ip地址版本
print(IPy.IP('10.0.0.0/8').version())
print(IPy.IP('::1').version())

# 通过指定网段输出该网段的ip个数和所有的ip地址清单
ip = IPy.IP("10.26.33.0/24")
print(ip.len())

for x in ip:
    print(x)

# 根据ip和掩码产生网段格式
print(IPy.IP('10.26.33.0').make_net('255.255.255.0'))
print(IPy.IP('10.26.33.0/255.255.255.0', make_net=True))
print(IPy.IP('10.26.33.0-10.26.33.255', make_net=True))

# 判断ip地址是否在一个网段中
print(IPy.IP('10.26.33.107') in IPy.IP('10.26.33.0/24'))
print(IPy.IP('10.26.34.107') in IPy.IP('10.26.33.0/24'))


# 生成ip地址池
def makeIpPool(startIP, lastIP, IPv6=False):
    IPver = 6 if IPv6 else 4
    intIP = lambda ip: IPy.IP(ip).int()  # 将ip地址转换为整型模式
    ipPool = set()
    for ip in range(intIP(startIP), intIP(lastIP)):
        ipPool.add(IPy.intToIp(ip, IPver))
    print(len(ipPool))
    print(ipPool)


makeIpPool('10.26.33.250', '10.26.33.255')
makeIpPool('fe80:0000:0000:0000:9e96:b5f6:393a:6c5f','fe80:0000:0000:0000:9e96:b5f6:393a:ffff',6)


#lambda匿名函数

f = lambda: "Hello, world!" #以下的 lambda 函数没有参数
print(f())  # 输出: Hello, world!

x = lambda a : a + 10 #以下实例使用 lambda 创建匿名函数，设置一个函数参数 a，函数计算参数 a 加 10，并返回结果
print(x(5))

x = lambda a, b : a * b #lambda 函数也可以设置多个参数，参数使用逗号隔开，以下实例使用 lambda 创建匿名函数，函数参数 a 与 b 相乘，并返回结果
print(x(5, 6))

x = lambda a, b, c : a + b + c #以下实例使用 lambda 创建匿名函数，函数参数 a、b 与 c 相加，并返回结果
print(x(5, 6, 2))

numbers = [1, 2, 3, 4, 5] #lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6, 7, 8] #使用 lambda 函数与 filter() 一起，筛选偶数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4, 6, 8]

from functools import reduce #下面是一个使用 reduce() 和 lambda 表达式演示如何计算一个序列的累积乘积

numbers = [1, 2, 3, 4, 5]

# 使用 reduce() 和 lambda 函数计算乘积
product = reduce(lambda x, y: x * y, numbers)

print(product)  # 输出：120
