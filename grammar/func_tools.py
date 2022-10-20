from functools import partial


def add(a, b, *args, **kwargs):
    print(a+b)
    print(args)
    print(kwargs)

p = partial(add, 1, 2, 3, 4, c=1, d=2)


if __name__ == '__main__':
    add(1, 2, 3, 4, c=1, d=2)
    print("*" * 30)
    p()