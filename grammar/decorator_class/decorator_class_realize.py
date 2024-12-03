"""
1. __call__ 实现
2. 普通类实现
总结：decorator 本质 @ 符号，将被装饰的函数作为参数传入，decorator调用对应的方法进行处理。
"""


class CallDecorator:

    def __call__(self, *args, **kwargs):
        print(f"__call__ execute")
        func = args[0]
        func()


@CallDecorator()
def execute_func():
    print(f"func executed")


class ClassDecorator:

    def __init__(self, func):
        print(f"__init__ execute")
        func()


@ClassDecorator
def execute_func1():
    print(f"func1 executed")


if __name__ == '__main__':

    print(execute_func1)
    print(1)