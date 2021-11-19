"""
type 三参数都传，就是创建一个类，参数说明：1.类名 2. 继承自谁 3. 类属性
https://docs.python.org/zh-cn/3.6/library/functions.html#type
"""


class Test:

    a = 1


t = type('Test1', (object,), {"a": 1})


class Test2(t):

    b = 2


if __name__ == '__main__':
    print(type(Test()))    # <class '__main__.Test'>
    print(t)    # <class '__main__.Test'>
    print(Test2.a)  # 1. 继承了t类的a属性，

    import inspect
    print(inspect.getmembers(t))




