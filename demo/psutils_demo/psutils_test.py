import datetime

import psutil
import socket
from collections import defaultdict

def cpu_info():
    print(psutil.cpu_times())
    # CPU使用率
    print(psutil.cpu_percent(interval=0.5))


def memory_info():
    print(f"内存信息: {psutil.virtual_memory()}")
    print(f"内存占用百分比: {psutil.virtual_memory().percent}")
    # 虚拟内存
    psutil.swap_memory()


def disk_info():
    print(f"磁盘信息: {psutil.disk_partitions(all=True)}")
    try:
        print(f"指定磁盘信息: {psutil.disk_usage('/')}")
    except OSError as e:
        print(f'路径不存在：{e=}')
    print(f"磁盘总大小: {psutil.disk_usage('/').total // (1024 * 1024 * 1024)}")
    print(f"磁盘使用: {psutil.disk_usage('/').used // (1024 * 1024 * 1024)}")


def network_info():
    network_dict = psutil.net_if_addrs()
    for network in network_dict.values():
        print(network[0].address)


def datetime_demo():
    ret = datetime.datetime.now() + datetime.timedelta(days=30)
    datetime.datetime.strptime()
    print(ret)


def default_dict_demo():
    list_data = [(1, 'a'), (2, 'b')]
    d = defaultdict(dict)
    for first, second in list_data:
        d[first] = second
    print(d)


if __name__ == '__main__':
    # cpu_info()
    memory_info()
    # disk_info()
    # network_info()
    # print(socket.gethostname())
    # print(socket.gethostbyname_ex(socket.gethostname()))
    # print(socket.gethostbyname(socket.gethostname()))
    # print(socket.gethostbyaddr("127.0.0.1"))
    # datetime_demo()
    # default_dict_demo()