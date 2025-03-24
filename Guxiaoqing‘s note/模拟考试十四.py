list = [467, 4, -45, 34, 51, 90]
list2 = [16, 23, 980, 45]

lb = list + list2 #合并列表
lb.sort(reverse=True)
print(lb)
lb.sort() #倒序排序
print(lb) #打印列表

age = int(input("请输入你的成绩："))
if age >= 90:
    ticket_price = "优秀"
elif age >= 80:
    ticket_price = "良好"
elif age >= 70:
    ticket_price = "合格"
else:
    ticket_price = "不及格"
print("你的成绩为:", ticket_price)
