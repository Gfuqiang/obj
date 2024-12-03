"""
empty类用来判断是否传入参数，因为None有可能作为有效参数使用。
"""

class empty:

    pass


def func1(data=empty):
    if data is empty:
        print("没有传入data参数")
    else:
        print(f"传入data参数：{data}")


if __name__ == '__main__':
    func1()
    # 根据对象获取类名
    em = empty()
    print(em.__class__.__name__)