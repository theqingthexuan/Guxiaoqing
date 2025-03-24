# pip install psutil 安装系统监控库
# 使用psutil库
import psutil

# 内存
mem = psutil.virtual_memory()
print(mem)
# 系统总计内存
zj = float(mem.total / 1024 / 1024 / 1024)
# 系统已使用内存
ysy = float(mem.used / 1024 / 1024 / 1024)
# 系统空闲内存
kx = float(mem.free / 1024 / 1024 / 1024)
# 打印结果
print('系统总计内存：%d.4GB' % zj)
print('系统已经使用内存：%d.6GB' % ysy)
print('系统空闲内存：%d.8GB' % kx)

# 获取CPU所有逻辑信息
print(psutil.cpu_times(percpu=True))
# 获取CPU逻辑个数的信息
print("逻辑个数CPU个数：%d" % psutil.cpu_count())
# 获取CPU物理个数的信息
print("物理CPU个数：%d" % psutil.cpu_count(logical=True))
# CPU使用率
cpu = (str(psutil.cpu_percent(1))) + '%'  # 一秒获取一次cpu使用率
print("CPU使用率：" + cpu)  # 打印CPU使用率结果

# 获取网卡信息
import psutil

#获取磁盘信息
part =psutil.disk_partitions()
for i in part:
    print(i)
dk = psutil.disk_usage('/')
print(dk)
#总磁盘
total = dk.total / 1024 / 1024 / 1024
used = dk.used / 1024 / 1024 / 1024
free = dk.free / 1024 / 1024 / 1024
print('系统总计硬盘：%d.4GB' % total)
print('系统已经使用硬盘：%d.4GB' % used)
print('系统空闲硬盘：%d.6GB' % free)
print('硬盘使用率：%s%%' % dk.percent)
# 获取网络接t口状态
#获取网络总io信息
print(psutil.net_io_counters())

#发送数据包
print("发送数据字节：",psutil.net_io_counters().bytes_sent,"bytes")
#接收数据包
print("接收数据字节：",psutil.net_io_counters().bytes_recv,"bytes")
#输出网络每个接口信息
net_counter = psutil.net_io_counters(pernic=True)
print(type(net_counter))
for i in net_counter:
    print("网卡："+i+",网卡信息：",net_counter[i])

# 数据单位
# b:bit（位） B:Byte(字节) 1B=8b
# MB：兆 1MB=1024B 1GB=1024MB 1TB=1024GB

# 列表
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list[0])  # 打印第一位
print(list[1])
print(list[2])
print(list[-1])
print(list[-2])
print(list[-3])

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[0:4])  # 从0打印到4号位

print("第三个元素为：", list[2])  # 更新元素
list[2] = 2001
print("更新后的第三元素为：", list[2])

list1 = ['Google', 'Runoob', 'Taobao']
print("原来的列表 : ", list1)
list1.append('Baidu')  # 在最后面添加一个字符Baidu
print("更新后的列表 : ", list1)

list2 = ['Google', 'Runoob', 1997, 2000]

print("原始列表 : ", list2)
del list2[2]
print("删除第三个元素 : ", list2)


# 查询所有进程信息，记得第一行要先调用库（import psutil，我这前面调用了就不调多一次了)
def query_process_info():
    # 获取所有进程信息
    processes = psutil.process_iter()
    for process in processes:
        # 输出进程的名称、pid、状态和用户名
        print(f"进程名称：{process.name}，pid：{process.pid}，状态：{process.status}，用户名：{process.username}")


# 调用函数
query_process_info()

# 拉取subprocess库和psutil库，我前面已经拉取了就不再拉取了
import subprocess

# 创建新进程
subprocess.Popen(["notepad.exe"])
# 检测进程是否存在
process_name = "notepad.exe"
is_running = any(process.info['name'] == process_name for process in psutil.process_iter(attrs=['name']))
print(f"{process_name} is running: {is_running}")

# 终止进程
# 根据进程名称终止进程
process_name = "notepad.exe"
for process in psutil.process_iter(attrs=['name']):
    if process.info['name'] == process_name:
        process.terminate()
        print(f"Terminated{process_name}")
