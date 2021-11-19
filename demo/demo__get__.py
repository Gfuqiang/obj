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

if __name__ == '__main__':
    b = B()
    print(b.b)
    # sys.stdout.write(f'test content')
    # print(sys.modules)
    ready_event = threading.Event()
    for k, v in sys.modules.items():
        print(f'{k}: {v}')
