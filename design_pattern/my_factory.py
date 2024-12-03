"""
关键字：根据输入产出对应内容
工厂模式：
    1. 工厂方法 （根据传入信息、产出指定内容）
    2. 抽象工厂 （根据输入内容使用不同工厂方法返回结果，隐藏了工厂方法的调用逻辑。对调用者隐藏了工厂方法的细节）

场景：
    1. 想要追踪对象的创建
    2. 想要将对象的创建和使用解耦时
"""

"""
工厂方法
对实例的创建进行隐藏，根据传入内容，返回内容。
example：根据传入文件类型，读取文件内容，并进行返回。提供json，xml处理。
"""
import json


class HandleJSON:

    def __init__(self, filepath):
        self.data = {}
        with open(filepath, 'r') as f:
            self.data = json.load(f)

    @property
    def handle(self):
        # 返回工厂结果
        return self.data


class HandleTXT:

    def __init__(self, filepath):
        self.data = ''
        with open(filepath, 'r') as f:
            self.data = f.read()

    @property
    def handle(self):
        # 返回工厂结果
        return self.data


def create_factory(filepath: str):
    # 根据逻辑判断返回对应工厂，工厂方法，返回工厂。
    if filepath.endswith('.json'):
        obj = HandleJSON
    elif filepath.endswith('.txt'):
        obj = HandleTXT
    else:
        raise ValueError(f'file: {filepath} not is endswith of json or txt')
    return obj(filepath)


def connect_to(file_path):
    # 处理工厂实例化过程中的问题
    factory = None
    try:
        factory = create_factory(file_path)
    except Exception as e:
        print(e)
    return factory


def main():
    # 传入需求，获取工厂实例
    factory = connect_to('./1.json')
    # 获取工厂产出结果
    result = factory.handle
    print(result)


"""
抽象工厂：
    抽象工厂设计模式是抽象方法的一种泛化。概括来说，一个抽象工厂是（逻辑上的）一组工厂方法，
    其中的每个工厂方法负责产生不同种类的对象
"""


