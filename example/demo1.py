def func1():
    try:
        1/ 0
    except Exception as e:
        raise FileNotFoundError(f'{e}: 111')
    return 1

def func2():
    try:
        e = func1()
        print(e)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    func2()