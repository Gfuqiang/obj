import functools

one_flag = False


@functools.lru_cache
def execute(num: int):
    global one_flag
    if num == 1:
        one_flag = True
    else:
        one_flag = False
    return num, one_flag


if __name__ == '__main__':
    print(execute(num=1))
    print(execute(num=2))
    print(execute(num=1))
    print(execute.cache_info())
