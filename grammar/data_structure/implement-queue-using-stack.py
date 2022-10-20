"""
使用栈实现队列
栈（后进先出）实现队列（先进先出），要使用两个栈，将第一个栈数据放入第二个栈数据就实现了先进先出
"""
from collections import deque


class Stack:

    def __init__(self):
        self.items = deque()

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty deque")

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


class Queue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, val):
        self.s1.push(val)

    def pop(self):
        # s2栈是空的，将s1中的数据添加到s2中
        if not self.s2.empty():
            return self.s2.pop()
        while not self.s1.empty():
            self.s2.push(self.s1.pop())
        return self.s2.pop()

    def empty(self):
        return self.s1.empty() and self.s2.empty()


def test_stack():

    stack = Stack()
    print(stack.empty())
    assert stack.empty(), "stack need is empty"
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    print(stack.empty())
    print(stack.pop())
    print(stack.empty())


def test_queue():
    q = Queue()
    assert q.empty(), "ques shod is empty"
    q.push(1)
    q.push(2)
    q.push(3)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    assert q.empty(), "ques shod is empty"


if __name__ == '__main__':
    # test_stack()
    test_queue()
