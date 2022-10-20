"""
实现一个栈， 后进先出
"""
import collections


class Stack:

    def __init__(self):
        self.stack = collections.deque()

    def append(self, val):
        self.stack.append(val)
        return self.stack

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return len(self.stack) == 0


if __name__ == '__main__':
    stack = Stack()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(stack.stack)
    print(stack.pop())
    print(stack.pop())
    print(f"len: {stack.empty()}")
    print(stack.pop())
    print(f"len: {stack.empty()}")


