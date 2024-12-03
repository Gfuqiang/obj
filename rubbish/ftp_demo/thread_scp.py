"""
多线程scp，是否受网络瓶颈影响
"""
import os
from threading import Thread


def scp_dir(ip, target_path='/root'):
    dir_name = 'scp_dir'
    ret_val = os.system(f'scp -r {dir_name} root@{ip}:{target_path}')
    if ret_val != 0:
        print(f'scp fail ret val:{ret_val}')
    print(ip)
    print(f'scp success ! ! !')


if __name__ == '__main__':
    ip_list = ['10.80.5.80', '10.80.15.138']
    threads = []
    for ip in ip_list:
        t = Thread(target=scp_dir, args=(ip, ))
        t.start()
        threads.append(t)
    for th in threads:
        th.join()


