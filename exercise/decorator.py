def repeat(parameter):
    def decorator(func):

        def wrapper(*args, **kwargs):
            print(f'parameter: {parameter}')
            print('run wrapper func')
            return func(*args, **kwargs)


        return wrapper
    return decorator

@repeat(555)
def my_func(*args, **kwargs):
    print(f'run my_func: {args}')
    return args


if __name__ == '__main__':
    # d = re(my_func)
    # result = d(1)
    result = my_func(1)
    print(result)
