"""
观察者模式
要素：
1. 观察者添加，移除
2. 有事件或判断触发通知函数的执行
3. 在通知函数中调用观察者的函数达到通知的目的
"""


class Publisher:

    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print(f"add fail: {observer} exist")

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError as e:
            print(f"remove fail: {observer} not exist")

    def notify(self):
        # 通知订阅者
        [observer.notify(self) for observer in self.observers]


class DefaultFormatter(Publisher):

    def __init__(self, name):
        super(DefaultFormatter, self).__init__()
        self.name = name
        self._data = 0

    def __str__(self):
        return f"{type(self).__name__}, {self.name}, data: {self._data}"

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, values):
        # 触发通知订阅者事件
        try:
            self._data = int(values)
        except Exception as e:
            print(f"To int error")
        else:
            self.notify()


class HexFormatter:

    def notify(self, publisher):
        # 订阅者执行的动作
        print(f"{type(self).__name__}, {publisher.name}, data:{hex(publisher._data)}")


class BinaryFormatter:

    def notify(self, publisher):
        # 订阅者执行的动作
        print(f"{type(self).__name__}, {publisher.name}, data:{bin(publisher._data)}")


def main():
    # 给data赋值触发通知观察者事件，调用对应观察者要执行动作的方法。（add，remove添加删除观察则）
    df = DefaultFormatter('test')
    print(df)
    hf = HexFormatter()
    bf = BinaryFormatter()
    df.add(bf)
    df.add(hf)
    df.data = 3
    print()
    print(df)
    print()
    df.data = 4
    print()
    print(df)
    df.data = 'hello word'
    print()

    df.data = 15.8


if __name__ == '__main__':
    main()
