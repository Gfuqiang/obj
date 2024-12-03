import time, functools, inspect


def func_time_watch(took_=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            if inspect.isgeneratorfunction(func):
                result = list(func(*args, **kwargs))
            else:
                result = func(*args, **kwargs)
            end = time.perf_counter()
            took_time = round(end - start, 2)
            print(f'{func.__name__} took {took_time}, {args=}')
            if took_:
                return result, took_time
            else:
                return result
        return wrapper
    return decorator
