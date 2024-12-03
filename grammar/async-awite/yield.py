"""
生成器，包含yield的函数被称为生成器
send方法默认值为None，不带参数时和next相同都是获取返回值，但是带参数时就会将参数赋值给yield左边表达式并返回该值。
生成器调用的第一个方法必须是next和不带参数的send。
"""


def generator():
    for i in range(1, 10):
        # next 调用生成器。yield 会在这里返回右边的值，并记住执行位置。调用生成器的send方法会将值传递到yield左边也就是这里的num
        num = yield i
        if num is None:
            num = 0
        print(f'count: {num + i}')


def generator_one():

    a = 1
    yield a
    a = 2
    yield a


def test_generator():
    gen = generator()
    print(f'first next func: {next(gen)}')
    print(f'first send func: {gen.send(5)}')
    print(next(gen))
    print(next(gen))
    print(gen.send(1))


def test_generator_one():
    gen = generator_one()
    # 分别调用一个和两个next方法看效果
    # 每调用一个next 代码会从上一个yield处开始执行。从而证明调用一次yield代码会停止在yield那里。
    print(next(gen))
    print(next(gen))


def main():
    # test_generator_one()
    test_generator()


if __name__ == '__main__':
    main()