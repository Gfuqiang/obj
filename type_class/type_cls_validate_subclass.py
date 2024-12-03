"""
例子来源于effective python 一书
元类用作验证子类属性
"""


class ValidateClass(type):

    def __new__(meta, name, bases, class_dict):
        if bases != (object, ):
            # 判断不是基类，针对基类的子类进行操作
            print(f'{meta=}, {name=}, {bases}, {class_dict}')
            if class_dict.get('realize') is not None:
                raise ValueError(f'realize attribute must is None')
        return type.__new__(meta, name, bases, class_dict)


class BaseClass(object, metaclass=ValidateClass):

    sides = None

    @classmethod
    def _func(cls):
        print(f'sides: {cls.sides}')


print('定义RealizeClass类前')


class RealizeClass(BaseClass):

    # 元类校验了该属性必须为None，否则抛出异常
    print(f'属性定义前')
    realize = 'realize'
    # realize = None
    print(f'属性定义后')

    print(f'类方法定义前')

    @classmethod
    def _func_(cls):
        print(f'realize: {cls.realize}')
        print(f'类方法中')


if __name__ == '__main__':
    base = RealizeClass()

