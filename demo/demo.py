import collections
import copy
import datetime
import json
import os
import pprint
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from functools import reduce
from pathlib import Path

import pandas as pd
import validators


def decorator(func):
    # def out_wrapper(func):
    def wrapper(*args, **kwargs):
        # print(f'parameter: {parameter}')
        print(22)
        func()
    return wrapper
    # return out_wrapper


# @decorator
def func():
    print(1)


def parameter_decorator(parameter):
    def out_wrapper(func):
        def wraperr(*args, **kwargs):
            print(f'parameter: {parameter}')
            func()
        return wraperr
    return out_wrapper


@parameter_decorator('parameter')
def func1():
    print('aaa')


def filter_func():
    print(list(filter(lambda x: x % 2 == 0, range(10))))


def zip_func():
    # [(1, 3), (2, 4), (3, 5)]
    print(list(zip([1, 2, 3], [3, 4, 5])))
    # [(1, 2, 3), (3, 4, 5)]
    print(list(zip(*list(zip([1, 2, 3], [3, 4, 5])))))


def map_func():
    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    print(list(map(lambda x: x * x, range(10))))
    # 将可迭代对象传入func中，以长度最短的对象为准。
    # [5, 7, 9, 7]
    print(list(map(lambda x, y: x + y, [1, 2, 3, 0], [4, 5, 6, 7, 8])))


def reduce_func():
    # 24 进行一个累加计算,将结果作为其中一个参数和后续数据进行计算，Ex: (((1*2)*3)*4)
    print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))


def quick_sort(list_data, start, end):

    if start >= end:
        return

    mid_data = list_data[start]

    left = start
    right = end

    while right > left:
        # 这里必须先移动右边的指针，必须先从右边开始找，因为标准值取得是列表第一个元素。
        while list_data[right] >= mid_data and left < right:
            right -= 1
        list_data[left] = list_data[right]
        while list_data[left] <= mid_data and left < right:
            left += 1
        list_data[right] = list_data[left]
    list_data[left] = mid_data

    quick_sort(list_data, start, left - 1)
    quick_sort(list_data, left + 1, end)

    return list_data


def quick_sort1(list_data, left, right):

    if left >= right:
        return

    mid_data = list_data[left]
    l = left
    r = right
    while r > l:
        while r > l and list_data[r] >= mid_data:
            r -= 1
        list_data[l] = list_data[r]
        while r > l and list_data[l] <= mid_data:
            l += 1
        list_data[r] = list_data[l]
    list_data[l] = mid_data

    quick_sort(list_data, left, l - 1)
    quick_sort(list_data, l + 1, right)

    return list_data


def multipliers():
    return [lambda x: i * x for i in range(4)]


def merge_sort(list_data):

    if len(list_data) <= 1:
        return list_data
    mid = len(list_data) // 2
    left = merge_sort(list_data[:mid])
    right = merge_sort(list_data[mid:])

    return merge_list(left, right)


def merge_list(left, right):
    """
    疑问： 该方法传入两个数组不能合并成有序的新数组嘛？ 不能 [5, 2], [4, 1],该方法合并完是[4, 1, 2, 5]. 该方法合并两个有序的数组
    新数组才是有序的。或者合并两个一个元素的数组，归并排序就是这样，将单个元素的数组合并后变为有序，在讲有序的数组进行合并。
    :param left:
    :param right:
    :return:
    """

    new_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1

    if i == len(left):
        new_list.extend(right[j:])
    else:
        new_list.extend(left[i:])

    return new_list


def fibonacci(n):

    ret_list = [1]
    if n <= 0:
        return []
    if n == 1:
        return ret_list
    init = 1
    while init <= n:
        ret_list.append(init)
        init = ret_list[len(ret_list) - 1] + ret_list[len(ret_list) - 2]
    return ret_list


def fibonacci_recursion(n):

    if n == 1 or n == 2:
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n - 2)


def get_greatest_common_divisor(first, second):
    # 获取两个数的最大公约数

    if first == second:
        return first

    min_num = min([first, second])
    common_divisor = 0
    for i in range(min_num, 0, -1):
        if first % i == 0 and second % i == 0:
            common_divisor = i
            break
    return common_divisor


def get_greatest_common_divisor_two(first, second):
    # 获取两个数的最大公约数。 碾转相除发，两个数 a > b 的情况下，a 除以b得到余数c和b的公约数,与a和b的最大公约数相同。
    # 使用递归的方式计算
    min_num = min([first, second])
    max_num = max([first, second])
    if max_num % min_num == 0:
        return min_num
    return get_greatest_common_divisor_two(max_num % min_num, min_num)

def func1(a, **kwargs):
    print(a)
    print(kwargs)

def generate(input):
    if not input:
        return
    yield input


def func2():
    for i in range(5):
        if i == 1:
            yield from generate(i)
        return

class ArgumentClass:

    def __init__(self, a):
        self.a = a

    def __call__(self, *args, **kwargs):
        print(self.a)
        return self.a

import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(2, result='execute')
    print('... World!')

import threading


def singleton_thread_safe(cls):
    instances = {}
    lock = threading.Lock()

    print(id(lock))

    def get_instance(*args, **kwargs):
        with lock:
            time.sleep(2)
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]
    return get_instance


@singleton_thread_safe
class StayInstanceClass:

    ...


def create_instance(sleep_time):
    time.sleep(sleep_time)
    print(threading.current_thread().name)
    return StayInstanceClass()


def multithread_test():
    with ThreadPoolExecutor() as execute:
        for result in execute.map(create_instance, [1, 1, 1]):
            print(result)
        # future = execute.submit(create_instance)
        # future1 = execute.submit(create_instance)
        # print(future1.result())
        # print(future.result())

TERM = os.getenv('TERM', '')
IS_ANSI_TERMINAL = TERM in (
    'eterm-color',
    'linux',
    'screen',
    'vt100',
) or TERM.startswith('xterm')


class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'


def print_error_msg(msg):
    print(Colors.RED + msg + Colors.RESET)
    print(123123)


def minimize():
    current = yield
    print(f'first :{current}')
    while True:
        val = yield current
        print(f'second :{current}')
        print(f'{val=}')
        current = min([val, current])
        print(f'运行1次')

def duplicate_removal():

    data = [
  [
    {
      "destinationTranslate": "a.waf.cn",
      "destinationPortTranslate": "",
      "destination": "a.x.com",
      "destinationPort": ""
    },
    {
      "destinationTranslate": "112.31.4.187",
      "destinationPortTranslate": "",
      "destination": "a.waf.cn",
      "destinationPort": None
    },
    {
      "destinationTranslate": "10.1.1.1",
      "destinationPortTranslate": "",
      "destination": "112.31.4.187",
      "destinationPort": None
    }
  ],
  [
    {
      "destinationTranslate": "a.waf.cn",
      "destinationPortTranslate": "",
      "destination": "a.x.com",
      "destinationPort": ""
    },
    {
      "destinationTranslate": "112.31.4.187",
      "destinationPortTranslate": "",
      "destination": "a.waf.cn",
      "destinationPort": None
    },
    {
      "destinationTranslate": "10.1.1.2",
      "destinationPortTranslate": "",
      "destination": "112.31.4.187",
      "destinationPort": None
    }
  ],]
    df = pd.DataFrame(data)
    new_df = df.drop_duplicates()
    print_error_msg(new_df)

def is_valid_domain(domain):
    try:
        ret = validators.domain(domain, consider_tld=True)
        if ret is True:
            return True
    except Exception as e:
        ...
    return False

def generate_func(one):
    # if one == 1:
    #     yield
    return
    for index, i in enumerate(range(10)):
        if index == 2:
            return
        yield i

def generate_main():
    yield from generate_func(2)


def custom_json_serializer():
    data = {
        "name": "Tom",
        "data": datetime.datetime.now()
    }

    def date_serializer(obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d")
        return TypeError("type not serializable")

    json_data = json.dumps(data, default=date_serializer)
    print(json_data)



if __name__ == '__main__':
    # print_error_msg('error message')
    # duplicate_removal()
    # print(is_valid_domain('domain.com.cn'))
    custom_json_serializer()


