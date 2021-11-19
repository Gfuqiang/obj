"""
获取第n个斐波那契数
"""


def fib_repeat(n):
    # 递归性能较差
    if n <= 1:
        return n
    return fib_repeat(n - 1) + fib_repeat(n - 2)


def fib(n):
    if n <= 1:
        return n
    first = 0
    second = 1
    for _ in range(n):
        first, second = second, first + second
    return second


if __name__ == '__main__':
    result = fib(70)
    print(result)
