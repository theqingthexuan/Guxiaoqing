
import difflib  # 读取俩个文件的内容

with open('file1.txt', 'r') as f1:
    text1 = f1.read()

with open('file2.txt', 'r') as f2:
    text2 = f2.read()

# 使用Differ 类生成俩个文件的差异
diff = difflib.Differ()
diff_result = list(diff.compare(text1.splitlines(keepends=True), text2.splitlines(keepends=True)))

# 输出差异内容
for line in diff_result:
    print(line)

d = difflib.HtmlDiff()
with open("passwd.html", 'w') as f:
    f.write(d.make_file(text1, text2))


# 1、新建一个变量message,将一条消息赋给该变量，并将其打印出来
message = "Hello, World!"
print(message)

# 2、给定列表my_list = ["honda", "yanaha", "suzuki"],进行以下操作：
# 步骤1：删除该列表中最后一个元素
# 步骤2：修改第一个元素为"Honda"
# 步骤3：在列表的末尾插入一个元素“ducat”。
# 步骤4：打印该列表
my_list = ["honda", "yanaha", "suzuki"]
# 删除列表中最后一个元素
my_list.pop()
# 修改第一个元素为"Honda"
my_list[0] = "Honda"
# 在列表的末尾插入一个元素"ducati"
my_list.append("ducati")
# 打印列表
print(my_list)

# 3、让用户输入分数，如果分数大于等于90分，则输出“A”；如果分数大于等于80分且小于90分，则输出“B”；如果分数大于等于70分且小于80分，则输出“C”；如果分数小于70分，则输出“D”。
# 获取用户输入的分数
score = int(input("请输入分数: "))
# 根据分数输出相应的等级
if score >= 90:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
else:
    grade = "D"
# 输出等级
print("你的等级是:", grade)


# 4、打印输出从1到100的所有奇数，每隔10个数换一行
# 定义一个函数来打印奇数
def print_odd_numbers():
    for i in range(1, 101):
        if i % 2 != 0:
            print(i, end="\t")
        if i % 20 == 0:
            print("\n")


# 调用函数打印奇数
print_odd_numbers()


# 5、按下列要求创建类：（30分）
# 定义一个Dog类，在该类中定义init方法添加两个属性：name(名字 )和age(年龄)，
# 方法定义：__init__(self,name,age)，通过Dog类创建一个实例my_dog,并打印输出实例的属性，
# 输出格式为："我的小狗叫xxx，已经yyy岁了。"
# 示例：我的小狗叫Willie，已经6岁了
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建 Dog 类的实例 my_dog
my_dog = Dog("Willie", 6)
# 打印实例的属性
print("我的小狗叫", my_dog.name, "，已经", my_dog.age, "岁了")
