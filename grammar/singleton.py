"""
单例: 实现单例，调用传入不同值，对象都是同一个
本质内存中的对象没有重新创建，但是属性已经变更了
"""


class A:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_singleton'):
            setattr(A, '_singleton', super().__new__(cls))
        return cls._singleton

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    a = A(1)
    print(a.name)
    print(id(a))
    b = A(2)
    print(b.name)
    print(id(b))

