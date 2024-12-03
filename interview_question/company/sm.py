"""
赛目科技
1. 排序算法
2. 自己实现一个pow函数
"""


def my_pow(x, y):
    if x == 0:
        if y == 0:
            return 1
        if y < 0:
            raise ZeroDivisionError
        return 0
    else:
        if x < 0:
            if y <= 0:
                return x
        else:
            if y == 0:
                return 1
            else:
                return x ** y


if __name__ == '__main__':
    ret = my_pow(3, 2/4)
    print(ret)
