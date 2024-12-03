import multiprocessing
import time


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, variable):
        self.variable = variable


def create_singleton(parameter):
    s = Singleton(parameter)
    time.sleep(1)
    # s.variable = parameter
    print(s)
    print(f's update: {s.variable}')
    return s


def run(parameter):
    # pool
    # pools = multiprocessing.Pool(multiprocessing.cpu_count())
    # for result in pools.imap_unordered(create_singleton, parameter):
    #     print(result)
    # pools.close()

    p1 = multiprocessing.Process(target=create_singleton, args=(1,))
    p2 = multiprocessing.Process(target=create_singleton, args=(2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('execution is completed ')
    s = Singleton(3)
    print(s)
    print(s.variable)


class TestClass():

    class_property = None

    def __init__(self, arguments = 1):
        self._arguments = 0
        self.arguments = arguments

    @property
    def get_arguments(self):
        return self.arguments

    @get_arguments.setter
    def get_arguments(self, value):
        print(f'execute setter')
        self.arguments = value


if __name__ == '__main__':
    # s1 = Singleton()
    # s2 = Singleton()
    # print(id(s1))
    # print(id(s2))

    # multiprocessing
    # parameter = [ _ for _ in range(40)]
    # run(parameter)

    # Test
    t = TestClass()
    t.arguments = 1
    # 实现@get_arguments.setter 可以使用以下赋值规则
    t.get_arguments = 10
    print(t._arguments)
    print(t.arguments)
