class DataDescriptor:

    def __init__(self, one):
        self.one = one

    def __set__(self, instance, value):
        print(instance)
        print(value)

    # def __get__(self, instance, owner):
    #     return self.one


class DemoClass:

    dd = DataDescriptor(1)


if __name__ == '__main__':
    dc = DemoClass()
    print(dc.__dict__)
    print(dc.dd.one)