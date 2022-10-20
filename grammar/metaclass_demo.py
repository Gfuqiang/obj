class MyMeta(type):     # metaclass继承type

    def __new__(cls, *args, **kwargs):
        print(f'MyMeta.__new__ ======== custom')
        print(cls.__name__)
        print(*args)
        print(**kwargs)

    def __init__(self, *args, **kwargs):
        print(f'MyMeta.__init__ ======== custom')


class Foo(metaclass=MyMeta):

    def __new__(cls, *args, **kwargs):
        print(f'Foo.__new__ ======== custom')
        print(cls.__name__)
        print(*args)
        print(**kwargs)

    def __init__(self):
        print(f'Foo.__init__ ======== custom')

    def son_fun(self):
        pass


class SonFoo(Foo):

   def __init__(self):
       pass





