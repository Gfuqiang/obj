"""
众趣
1. is == 用法及区别
2. 上台阶，斐波那契数据
3. 判断列表中的质数
"""


def fabonacci(n):
    if n == 1 or n == 2:
        return 1
    return fabonacci(n - 1) + fabonacci(n - 2)


def get_prime(list_data):
    # 判断列表中的质数有哪些
    prime_data_list = []
    for item in list_data:
        if item in [1, 2, 3]:
            prime_data_list.append(item)
            continue
        mid = item // 2
        # 记录该数字是否是质数的指针。
        is_prime = False
        for i in range(2, mid):
            if item % i == 0:
                is_prime = True
                break
        if not is_prime:
            prime_data_list.append(item)
    print(prime_data_list)


def is_judge():

    a = 1000
    b = 1000

    e = 100
    f = 100

    g_list = [1000]

    a_str = "abc"
    b_str = "abc"

    # pycharm
    """
    使用python命令行时对于小整数[-5,256]区间内的整数,python会创建小整数对象池，这些对象一旦创建，就不会回收，所有新创建的在这个范围的整数都是直接引用他即可。所以造成在[-5,256]区间内的整数不同变量只要值相同，引用地址也相同。此范围外的整数同样遵循新建一个变量赋予一个地址
    """
    # 而在Pycharm或者保存为文件执行，结果是不一样的，这是因为解释器做了一部分优化。下面使用pycharm,即使整数超过256，使用is也是成立的。
    # 命令行中a is b应该是False
    print(f'a is b: {a is b}')
    print(f'a == b: {a == b}')
    print(f'e == f: {e == f}')
    print(f'e is f: {e is f}')
    print(f'a is g_list: {a is g_list[0]}')
    print(f'a == g_list: {a == g_list[0]}')
    # python中虽然字符串对象也是不可变对象,但python有个intern机制，简单说就是维护一个字典，这个字典维护已经创建字符串(key)和它的字符串对象的地址(value),每次创建字符串对象都会和这个字典比较,没有就创建，重复了就用指针进行引用就可以了。相当于python对于字符串也是采用了对象池原理。
    print(f'a str is b str: {a_str is b_str}')
    print(f'a str == b str: {a_str == b_str}')


c = 380


def func1():

    d = 380
    print(f'c is d: {c is d}')
    print(f'c == d: {c == d}')


if __name__ == '__main__':
    # ret = fabonacci(6)
    # print(ret)

    # list_data = [1, 3, 5, 7, 9, 10, 12, 13, 15]
    # get_prime(list_data)

    is_judge()
    func1()