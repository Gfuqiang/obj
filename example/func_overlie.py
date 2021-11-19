def func1():
    def func2():
        print(f'2 run')
        def func3():
            print(f'3 run')
            return 2
        return func3
    func2()
    return 1

if __name__ == '__main__':
    data = func1()
    print(data)