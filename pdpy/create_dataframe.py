import pandas as pd
import numpy as np

"""
构建DataFrame数据
"""


def dict_parameter():

    dict_data = {
        "a": pd.Series([1, 2, 3]),
        'b': pd.Series([4, 5])
    }

    # val 是list 时，长度必须一致，Series 时不是必须一致，会自动填充Nan值。
    dict_data = {
        "a": [1, 2, 3],
        'b': [4, 5]
    }

    print(pd.DataFrame(dict_data))


def multidimensional_array_parameter():
    """
    多维数组
    :return:
    """

    data = np.zeros((2, ), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
    data[:] = [(1, 2., 'Hello'), (2, 3., "World")]

    data = [[1, 2, 3], [4, 5]]

    print(pd.DataFrame(data))


def list_dict_parameter():
    """
    列表字典
    :return:
    """

    data = [{'a': 1, 'b': 2}, {'c': 3, 'a': 1}, {'d': 4}, {'a': [1, 2, 3, 4]}]
    print(pd.DataFrame(data))


def tuple_dict_parameter():
    """

    :return:
    """
    data = {
        ('a', 'b'): {('A', 'B'): 1, ('A', 'B'): 2}
    }
    data = pd.DataFrame(data)
    print(data)


def from_dict_parameter():
    """

    :return:
    """
    data = pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]))
    print(data)


if __name__ == '__main__':
    # dict_parameter()
    # multidimensional_array_parameter()
    list_dict_parameter()
    # tuple_dict_parameter()
    # from_dict_parameter()
