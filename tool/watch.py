import time, functools


def func_time_watch(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} took {round(end - start, 2)}')
        return result
    return wrapper
