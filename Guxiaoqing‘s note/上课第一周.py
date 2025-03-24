#典型int类型整数加法
"""
a=1
b=2
print(b+a)
"""
#字符串打印内容
"""
name=123
print("name")
print(name)
"""
#利用len和in元素查找（len）长度和（in）特定字符
"""
a="fafafsad"
print(len(a))
print("c"in a)

c=true
print(type(c))
"""

#字典类型
"""
a=[1,2,4,5,6,7,123]
print(a)
print(max(a))
print(min(a))

#字典取值
b={"name":'qing','length':176,'weight':80}
print(b['name'])
print(b)
print(type(b))
"""
#取元素
"""
a=[1,2,3,4,5,6,8]
print(a[6])#从零开始数第6位数
print(a[-6])#从零开始数第倒数第6位数
"""

#问答条件语句（elif为中间部分可以多个，if为开头，else为结束）（在此部分加上了while元素达成循环10次访问）
"""
i = 10
while i < 10:
    score = input('请输入你的分数：')
    score = int(score)
    if score >= 90:
        print("厉害")
    elif score < 60:
        print("不合格")
    else:
        print("还行，继续加油")
    i = i - 1
"""


#利用for函数写出的乘法表
for x in range(1,10):
    for y in range(1,x+1):
        print(f"{y}*{x}={x*y}".ljust(6),end='')
    print("")

