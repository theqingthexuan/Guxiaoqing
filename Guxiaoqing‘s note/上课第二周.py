"""
#打开资料
f = open("资料库/test.txt","r+")#r+代表权限打开文件可读可写，没有文件会报错。w+代表权限打开文件可读可写，如果没有文件会创建文件并覆盖
print(f.name)
"""

"""
#读取资料
content=f.read()
print(content)
"""

"""
#读取一二行
test01=f.readline()
test02=f.readlines()
print(test01)
print(test02)
"""

"""
#写入文件，插入
f.write("这是一个写文件测试")#这里面输入的参数会插入之前的文本
content=f.readline()
print(content)
f.close()
"""

"""
#跳过错误
try:#变量
    print(4)
    print(404)
except Exception:#如果发生了错误
    print("上面有错误")
else:#如果没有发生错误
    print("上面没错误")
finally:#无论错还是对都会执行
    print(5)
#提问：上面try的命令会出现在控制台吗？会跳到下面的print("上面有错误")吗？那print(3)会出现在控制台吗？
"""

"""
#函数应用和函数调用
def CS():
    length = float(input("请输入三角形的长度："))
    height = float(input("请输入三角形的高度："))
    weight = float(input("请输入三角形的宽度："))
    s = 0.5 * length * height
    c = length+height+weight

    print(f"这个三角形的面积是{s}")
    print(f"这个三角形的周长{c}")

print("现在执行函数功能")
CS()


def CS2(a,b):
    s = 0.5 * a * b
    return s
"""


#作业1,调用其他文本函数
import printing_function
printing_function.print_odd(100)


#作业2
f = open("资料库/test.txt","r+")#r+代表权限打开文件可读可写，没有文件会报错。w+代表权限打开文件可读可写，如果没有文件会创建文件并覆盖
print(f.name)
f.write("你好 "
        "我的名字叫顾小箐 "
        "今天是我第一次进行文件的操作 "
        "我成功啦 ")#这里面输入的参数会插入之前的文本
content=f.readline()
print(content)
f.close()
