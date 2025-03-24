import psutil
def query_process_info():
    # 获取所有进程信息
    processes = psutil.process_iter()
    for process in processes:
        # 输出进程的名称、pid、状态和用户名
        print(f"进程名称：{process.name}，pid：{process.pid}，状态：{process.status}，用户名：{process.username}")
#调用函数
query_process_info()
