"""
原型模式
    为对象创建一个副本
"""
import copy


class Book:
    # create book obj
    def __init__(self, name, price, **kwargs):
        self.name = name
        self.price = price
        self.__dict__.update(kwargs)

    def __str__(self):
        return f'{self.name} \n {self.price}'


class Prototype:
    # prototype class

    def __init__(self):
        self.object = {}

    def register(self, key, obj):
        self.object[key] = obj

    def unregister(self, key):
        del self.object[key]

    def clone(self, key, **kwargs):
        obj = self.object.get(key, None)
        if not obj:
            raise ValueError(f'incorrect object identifier:{key}')
        obj_copy = copy.deepcopy(obj)
        obj_copy.__dict__.update(**kwargs)
        return obj_copy


def main():
    # 创建初始对象
    book = Book('left', 25)
    # 创建原型类
    p = Prototype()
    key = '123'
    # 注册原始对象
    p.register(key, book)
    # copy原始对象，并进行修改。
    book_copy = p.clone(key, price=100)
    
    for i in (book, book_copy):
        print(i)


if __name__ == '__main__':
    main()