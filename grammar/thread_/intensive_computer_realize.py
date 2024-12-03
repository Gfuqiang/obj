"""
密集运算型任务在多线程中的情况
"""
import time

from tool.watch import func_time_watch
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


@func_time_watch(took_=True)
def factorize(number):
    # 运算函数

    for i in range(1, number + 1):
        if number % i == 0:
            yield i


def main():
    one_thread = 0  # 该时间是函数执行时间总和，不是任务执行完的耗时
    numbers = [21390791, 1214759, 15166371]
    # for item in numbers:
    #     ret, time = factorize(item)
    #     one_thread += time
    # print(f'{one_thread=}')
    try:
        with ThreadPoolExecutor() as executor:
            ret = executor.map(factorize, numbers)
        _ = [item[1] for item in ret]
        multithread = sum(_)
        print(multithread)
    except Exception as e:
        print(f'{e=}')
    # print(f'{multithread=}')


if __name__ == '__main__':
    main()
