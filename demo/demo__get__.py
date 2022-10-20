import sys
import threading
class A:

    def __get__(self, instance, owner):
        print(f'self: {self}')
        print(f'instance: {instance}')
        print(f'owner: {owner}')
        return instance


class B:

    b = 'a'
    a = A()

    def __init__(self):
        self.c = 'c'
        print(__name__)


def demo1():
    a = 1
    return a

def demo2():
    print(a)

if __name__ == '__main__':
    # b = B()
    # if isinstance(b, B):
    #     print('*' * 50)
    # print(b.b)
    # # sys.stdout.write(f'test content')
    # # print(sys.modules)
    # ready_event = threading.Event()
    # for k, v in sys.modules.items():
    #     print(f'{k}: {v}')

    a = '2'
    demo2()
        

