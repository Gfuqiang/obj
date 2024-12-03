"""
例子来源于effective python 一书
使用元类注册子类（为完成）
"""
import json
import pprint


class Serializer:
    """
    序列化字符串功能的类
    """
    def __init__(self, *args):
        self.args = args

    def serializer(self):
        return json.dumps({'args': self.args})


class Point2D(Serializer):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y)

    def __repr__(self):
        return f'Point2D: {self.x=}, {self.y=}'

    # def __str__(self):
    #     return f'{self.x=}, {self.y=}'


class Deserializer(Serializer):

    @classmethod
    def deserializer(cls, data):
        load_data = json.loads(data)
        return cls(*load_data['args'])


if __name__ == '__main__':
    point2d = Point2D(3, 5)
    # 下边代码会调用 __repr__方法
    print(point2d)
    print(point2d.serializer())
    dict_data = point2d.serializer()

