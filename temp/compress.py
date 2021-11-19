class TestClass():

    @classmethod
    def as_view(cls, *kwargs):
        print(111)
        def view():
            print(f'class name: {cls.__name__}')
        return view

    def __get__(self, instance, owner):
        print(owner)
        print(instance)
        print('This is class get method')


class TestMain():
    a = TestClass()

if __name__ == '__main__':
    main = TestMain()
    print(__path__[0])
    # print(main.a)