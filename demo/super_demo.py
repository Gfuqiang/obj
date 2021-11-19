class A:

    def func1(self, a):
        return a + 1


class B(A):

    cls_b = 'cls_property'

    def __init__(self, a):
        self.self_a = a

    def __getattr__(self, item):
        print(f'__getattr__ 被调用了！！！')
        print(f'__getattr__: {item}')
        return 'a'

    # def __getattribute__(self, item):
    #     print(f'__getattribute__ 被调用了！！！')
    #     print(item)
    #     raise AttributeError

    def func1(self, a):
        print(super(B, self).func1)
        return super().func1(a)


if __name__ == '__main__':
    b = B(1)
    a = b.__module__
    print(B.__module__)
    print(a)
    print(object())
    # print(B.cls_b)