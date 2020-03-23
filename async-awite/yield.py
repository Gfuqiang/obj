
def generator():
    for i in range(1, 10):
        num = yield i
        if num is None:
            num = 0
        print(f'count: {num + i}')


if __name__ == '__main__':
    gen = generator()
    print(next(gen))
    print(gen.send(5))
    print(next(gen))
    print(next(gen))
    print(gen.send(1))