def recursion(n):

    if n <= 2:
        return 1
    return recursion(n - 1) + recursion(n - 2)


def loop(n):
    a, b = 0, 1
    for i in range(n):
        print(b, end=' ')
        a, b = b, a + b


if __name__ == '__main__':
    for i in range(1, 10):
        print(recursion(i), end=' ')
    print()
    print('*' * 50)
    loop(10)