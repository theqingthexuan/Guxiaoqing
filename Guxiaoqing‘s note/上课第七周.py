age = int(input("请输入你的年龄："))
if age < 10:
    ticket_price = 10
elif age <= 18:
    ticket_price = 15
else:
    ticket_price = 20
print("你的票钱为:", ticket_price)


def calculate_ticket_price(age):
    if age < 10:
        ticket_price = 10
    elif age <= 18:
        ticket_price = 15
    else:
        ticket_price = 20
    return ticket_price


age = int(input("请输入你的年龄："))
ticket_price = calculate_ticket_price(age)
print(f"你的票钱为{ticket_price}")


def calculate_sum(N):
    sum = 0
    for i in range(1, N + 1):
        sum += i
    return sum


N = int(input("请输入一个大于 1 的数字："))
result = calculate_sum(N)
print("1 到", N, "的累加和为：", result)

import dns.resolver

# 输入域名地址
domain = input('请输入域名地址：')
# 指定查询类型为A记录
A = dns.resolver.resolve(domain, 'A')
# 通过response.answer方法获取查询信息
for i in A.response.answer:
    # 遍历回应信息
    for j in i.items:
        print(j)

import dns.resolver
import http.client

# 定于域名ip列表变量
iplist = []
# 自定义业务域名
appdomain = "www.baidu.com"


# 域名解析函数，解析成功IP将被追加到ip list
def get_iplist(domain=""):
    try:
        A = dns.resolver.resolve(domain, 'A')

    except Exception as e:
        print("dns resolver error:" + str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            # 追加到iplist列表
            iplist.append(j)
    return True


def checkip(ip):
    checkurl = str(ip) + ": 80"
    getcontent = ""
    # 定义http连接5秒超时（5）秒
    http.client.socket.setdefaulttimeout(5)
    # 创建http连接对象
    conn = http.client.HTTPConnection(checkurl)
    try:
        # 发起url请求，添加host主机头
        conn.request("GET", "/", headers={"Host": appdomain})
        r = conn.getresponse()
        # 获取URL页面前15个字符用来可用性校验
        getcontent = r.read(15)

    finally:
        # 监控URL页的内容一般是事先定义好的比如http 200等
        if getcontent == b"<!DOCTYPE html>":
            print(str(ip) + "[ok]")
        else:
            print(str(ip) + "[Error]")
        # 获取response的状态码
        print(r.reason)
        # 获取response的状态 ok或者error
        print(r.status)


if __name__ == "__main__":
    # 域名解析正确且至少返回一个IP
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print("dns resolver error.")
