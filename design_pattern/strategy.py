import pprint, time
from collections import namedtuple
from operator import attrgetter

"""
概述:
策略模式通常用在我们希望对同一个问题透明地使用多 种方案时。
如果并不存在针对所有输入数据和所有情况的完美算法，那么我们可以使用策略模式， 动态地决定在每种情况下应使用哪种算法。
现实中，在我们想赶去机场乘飞机时会使用策略模式(不同线路，不同工具)。

一般实现方式:
1. 分别定义不同的 strategy 类或方法
2. 实现一个上下文管理类或方法，通过一定条件来判断使用哪个 strategy（将strategy对象传入上下文管理中后调用）
    实现技巧：使用抽象类来控制 strategy class 实现统一方法，上下文管理者调用策略类实现的统一方法。
"""


def demo():
    # 按名称或数量排序，就是两种不同的策略
    stats = (('Ruby', 14), ('Javascript', 8), ('Python', 7),
                      ('Scala', 31), ('Swift', 18), ('Lisp', 23))

    ProgrammingLang = namedtuple('ProgrammingLang', 'name lang')
    pp = pprint.PrettyPrinter(indent=4)

    lang_list = [ProgrammingLang(name, lang) for name, lang in stats]
    lang_list = sorted(lang_list, key=attrgetter('name'))
    pp.pprint(lang_list)
    lang_list = sorted(lang_list, key=attrgetter('lang'))
    pp.pprint(lang_list)


LIMIT = 5
alter_message = 'too bad, you picked the slow algorithm :('


def pairs(seq):
    count = len(seq)
    for i in range(count):
        yield seq[i], seq[(i + 1) % count]


def all_unique_sort(s):
    if len(s) > 5:
        time.sleep(2)
        print(alter_message)
    s = sorted(s)
    for i, j in pairs(s):
        if i == j:
            return False
        else:
            return True


def all_unique_set(s):
    if len(s) < 5:
        time.sleep(2)
        print(alter_message)
        print(s)
    return False if len(set(s)) == len(s) else True


def strategy_func(s, strategy):
    return strategy(s)


def main():
    """
    根据输入字符串长度，使用不同的策略函数（判断字符串中是否有相同元素）
    :return:
    """
    while True:
        word = None
        while not word:
            word = input(f'Insert word (type quit to exit)> ')
            if word == 'quit':
                print('bey')
                return
            strategy_picked = None
            strategy_value = {'1': all_unique_sort, '2': all_unique_set}
            while strategy_picked not in strategy_value.keys():
                strategy = input(f'Choose strategy: [1] Use sort, [2] Use set')
                try:
                    ret = strategy_func(word, strategy_value[strategy])
                    print(f'{strategy_value[strategy].__name__} execute, ret: {ret}')
                except KeyError as e:
                    print(f'Input error')
                    break


if __name__ == '__main__':
    main()



