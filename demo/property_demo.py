class DecoratorClass:

    def __new__(cls, *args, **kwargs):
        print(f'create DecoratorClass Class')
        print(f'args: {args}')

    def __init__(self, func1):
        print(f'execute __init__ func')
        self.func1 = func1
        print(self.func1())


class A:

    @property
    def func1(self):
        print(1111)
        print(f'func1 execute')
        # return 1


if __name__ == '__main__':
    a = A()
    print(f'res: {a.func1()}')