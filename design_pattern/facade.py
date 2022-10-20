"""
外观模式：
    对系统细节进行隐藏和解耦
    提供一个外观类给客户端进行操作
    使用抽象基类对子系统必要方法进行定义。

    Ex:
        1. 定义系统基类，定义子类必须实现的方法
        2. 定义子系统并继承基类
        3. 定位外观类，外观类封装子系统的操作
        4. 外部调用外观类，实现系统的整体启动等
"""

from abc import ABCMeta, abstractmethod
from enum import Enum


State = Enum('State', 'new running sleeping restart zombie')


class Server(metaclass=ABCMeta):
    """
    metaclass=ABCMeta 配合 abstractmethod 使用，创建抽象类，子类必须实现装饰过的方法，且抽象类不能被直接实例化。
    系统抽象基类，规定系统应该有的方法
    """

    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def bot(self):
        pass

    @abstractmethod
    def kill(self):
        pass


class FilesServer(Server):
    """
    file子系统
    """

    def __init__(self):
        self.name = 'FileServer'
        self.status = State.new

    def bot(self):
        print(f'bot {self.name}')
        self.status = State.running

    def kill(self):
        print(f'kill {self.name}')
        self.status = State.restart if self.status else State.zombie

    # 子系统特殊功能
    def create_file_system(self):
        print(f'{self.name} create file system')


class NetWorkerServer(Server):
    """
    网络子系统
    """

    def __init__(self):
        self.name = 'NetWorkerServer'
        self.status = State.new

    def bot(self):
        print(f'bot {self.name}')
        self.status = State.running

    def kill(self):
        print(f'kill {self.name}')
        self.status = State.restart if self.status else State.zombie

    # 子系统特殊功能
    def start_network(self):
        print(f'start net work')


class OperatingSystem:
    """
    外观类，对细节进行隐藏
    """

    def __init__(self):
        self.fs = FilesServer()
        self.ns = NetWorkerServer()

    def open(self):
        self.fs.bot()
        self.ns.bot()

    def create_file_system(self):
        self.fs.create_file_system()

    def start_network(self):
        self.ns.start_network()


if __name__ == '__main__':
    opera = OperatingSystem()
    opera.open()
    opera.create_file_system()
    opera.start_network()