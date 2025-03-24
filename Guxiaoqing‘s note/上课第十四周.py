import socket, time
from time import sleep

socket.setdefaulttimeout(1)
import _thread as thread

socket.setdefaulttimeout(0.5)


# 单线程扫描
def scan(ip, port):
    print("")
    print('server %s,port: %s is scaning' % (ip, port))
    try:
        port = int(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((ip, port))
        if res == 0:
            print('Result:OPEN')
            print('')
        else:
            print('Res:CLOSE')
            print("")
        sock.close()
    except socket.gaierror:

        print("")
        print('Hostname could not be resolved.Exiting')
    except socket.error:
        print("")
        print("Can't connect to the server")


if __name__ == '__main__':
    scan('127.0.0.1', 445)


# 多线程扫描
def socket_port(ip, port):
    try:
        if port >= 65535:
            return
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            lock.acquire()
            print(ip, u':', port, u'端口开放')
            lock.release()
        s.close()
    except Exception as e:
        pass


def ip_scan(ip):
    """
    输入IP，扫描ip的0-65534端口情况
    """
    try:
        print(u'开始扫描 %s' % ip)
        start_time = time.time()
        for j in range(0, 660):
            for i in range(j * 100, 100 * (j + 1)):
                thread.start_new_thread(socket_port, (ip, int(i)))
            sleep(0.5)  # 休眠 防止线程创建的过多报错 （can_not_create_new_start_thread)
        print(u'扫描端口完成，总共用时 ： %.2f' % (time.time() - start_time))
    except Exception as e:
        print(u'扫描ip出错')


if __name__ == '__main__':
    lock = thread.allocate_lock()
    ip_scan('127.0.0.1')
