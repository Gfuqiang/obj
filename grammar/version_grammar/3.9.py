def merge_dict():
    """
    合并和更新字典
    :return:
    """
    d1 = {'a': 1, 'b': 1, 'c': 1}
    d2 = {'E': 0, 'F': 0, 'c': 0}
    dict_list = [('g', 100), ('h', 100)]
    d3 = {'aba': 1, 'abb': 2}
    # key值相同 | 后边覆盖前边
    print(d1 | d2)
    print(d2 | d1)
    # 增强赋值，同update方法
    d1 |= dict_list
    d1 |= d3
    print(d1)


def remove_str_prefix_or_suffix():

    init_str = '_str:'
    print(init_str.removeprefix('_'))
    print(init_str.removesuffix(':'))
    # 不修改原字符串
    print(init_str)


if __name__ == '__main__':
    # merge_dict()
    remove_str_prefix_or_suffix()