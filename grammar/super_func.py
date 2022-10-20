"""
python3 写法 super().__new__(cls)
python2 写法 super(B, self).__new__(cls)

super调用方法传参：
    1.传参根据父类方法需要的参数进行传递
    2.如果父类直接是type new方法传入cls，init方法什么都用不传

官网文档地址：https://docs.python.org/zh-cn/3.7/library/functions.html?highlight=super#super
"""


class A:

    def __new__(cls, *args, **kwargs):
        if issubclass(cls, type):
            print(111)
        else:
            print(222)
        return super(A, cls).__new__(cls)

    def __init__(self, a):
        self.a = a

        super(A, self).__init__()


class B(A):

    def __init__(self):
        # print(super().__init__(a))
        if isinstance(self, B):
            print(333)
        else:
            print(444)
        print(super())
        print(super(B))
        print(super(B, self))
        super().__init__(1)

        # super().__init__(self, a)


if __name__ == '__main__':
    b = B()
    b.a

