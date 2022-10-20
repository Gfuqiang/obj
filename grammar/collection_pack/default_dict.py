"""
dict 的一个子类
__missing__ 向字典中添加元素，参数为k，默认值 default_factory为v，添加到字典中。
"""

from collections import defaultdict


def simple_method():
    d_dict = defaultdict(list)
    d_dict.__missing__(1)
    print(d_dict)
    d_dict[1] = 1
    print(d_dict)

if __name__ == '__main__':
    simple_method()