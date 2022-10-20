import itertools
from collections import deque


def simple_method():

    d = deque([1, 2, 3], maxlen=4)
    d.append(4)
    d.appendleft(5)
    print(d.count(2))
    d.clear()
    d.extend([6, 7, 8, 9, 10])
    d.extendleft([11, 12, 13])
    d.reverse()
    d.rotate(3)
    print(d)


def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    print(11111)
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n


if __name__ == '__main__':

    moving_average([40, 30, 50, 46, 39, 44])
    simple_method()