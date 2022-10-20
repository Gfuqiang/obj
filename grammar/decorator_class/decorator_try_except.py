import requests, functools


def try_ex_decorator(func):
    @functools.wraps(func)
    def wrapper(p1):
        try:
            print(p1)
            func(p1)
            print(func)
        except Exception as e:
            print(f"异常是：{e}")
    return wrapper


@try_ex_decorator
def func(p1):
    rep = requests.get('http://10.80.5.138:8000/api/v1/cedar/cabinet/', timeout=10)
    print(rep.text)


def func1(a, b=None, **kwargs):
    print(a)
    print(b)
    print(kwargs)


if __name__ == '__main__':
    func(1111)
    # func1(1, **{"b":1, "c":4})