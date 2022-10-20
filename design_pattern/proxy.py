"""
代理模式:
1. 虚拟代理，将一个对象的初始化延迟到真正需要使用时进行，下边例子调用resource时才修改_resource属性。
2. 保护/防护代理，用于对处理敏感信息的对象进行访问控制
    将要保护的对象定义为代理的属性，调用代理来进行逻辑判断（校验信息等）起到保护作用
"""


class LazyProperty:

    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        print(f"method: {self.method}")
        print(f"method_name: {self.method_name}")

    def __get__(self, instance, owner):
        """
        当前类被实例化为类属性，并且调用时，会触发此方法。
        instance 为调用类属性的实例，没有则为None，owner为调用类属性所属的类。
        """
        print(f'execute: __get__ ')
        print(f'instance: {instance}')
        print(f'owner: {owner}')
        if not instance:
            return None
        value = self.method(instance)
        setattr(instance, self.method_name, value)
        return value


class Test:

    def __init__(self, y, x):
        self.x = x
        self.y = y
        self._resource = None

    @LazyProperty
    def resource(self):
        """
        类装饰器，将方法传入装饰器中。调用此方法就是实例化了resource。
        """
        print('initializing self._resource which is: {}'.format(self._resource))
        self._resource = tuple(range(5))
        return self._resource


if __name__ == '__main__':

    t = Test(1, 2)
    print(t.x)
    print(t.y)
    print(f't.__dict__: {t.__dict__}')
    print('*' * 50)
    print(t.resource)
    print(f't.__dict__: {t.__dict__}')
    print(t.resource)   # 第二次调用resource不会调用__get__ 方法。


