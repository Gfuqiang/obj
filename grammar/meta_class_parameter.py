"""
元类中的参数：
name: 派生类名称 str
base: 派生类基类 tulp
attrs: 派生类属性，方法 dict
"""


class DemoMetaClass(type):

    def demo_func(self, *args, **kwargs):
        pass

    def __new__(cls, name, base, attrs):
        print(f"{cls.__name__} 执行了")
        print(f"name: {name}\n"
              f"base: {base}\n"
              f"attrs: {attrs}")
        return super(DemoMetaClass, cls).__new__(cls, name, base, attrs)


class ImplementParentSuperClass:

    def __new__(cls, *args, **kwargs):
        print(args, kwargs)
        print(f"{cls.__name__} 执行了， ImplementParentSuperClass")
        return super(ImplementParentSuperClass, cls).__new__(cls)


class ImplementParentClass(ImplementParentSuperClass):

    def __new__(cls, *args, **kwargs):
        print(f"{cls.__name__} 执行了，ImplementParentClass")
        return super(ImplementParentClass, cls).__new__(cls, *args, **kwargs)

    def parent_func(self):
        pass


class ImplementClass(ImplementParentClass, metaclass=DemoMetaClass):

    c_a = 1

    def __init__(self, a, b, c=1):
        self.a = a
        print(f"super return: {super(ImplementClass, self).__init__()}")


if __name__ == '__main__':
    implement = ImplementClass("a", "b", c=1)
    # 调用类属性
    print(implement.c_a)
    # 调用实例属性
    print(implement.a)