"""
NotImplementedError 必须重写基类的抽象方法（要求派生类重载的方法），否则抛出异常
"""

class A:

    def raise_func(self, data):
        raise NotImplementedError(
            f"执行 NotImplementedError 异常 {self.__class__.__name__}"
        )


class B(A):

    def raise_func(self, data):
        print(f"重写raise func")



if __name__ == '__main__':
    b = B()
    v = b.raise_func(1)
    print(v)