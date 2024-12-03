import numpy as np

# zeros_array = np.zeros((2, 2, 2, 2))
# one_array = np.ones((2, 4), dtype=np.uint8)
# random_array = np.random.random((3, 4))
# kernel = np.ones((5, 5), dtype=np.float32)/25
# print(kernel)

"""
测试基础属性
"""


def get_array_attribute():
    array = np.arange(20).reshape(2, 5, 2)
    print(f'array: {array}')
    print(f'shape: {array.shape}')


def create_array_use_list_to_tuple():
    array = np.array([1, 2, 3])
    print(f'array: {array}')
    array = np.array((4, 5, 6))
    print(f'array: {array}')
    array = np.array([(7, 8), (9, 10)])
    print(f'array: {array}')


def create_array_use_func():
    """
    通常，数组的元素最初是未知的，但它的大小是已知的。
    因此，NumPy提供了几个函数来创建具有初始占位符内容的数组。
    这就减少了数组增长的必要，因为数组增长的操作花费很大。
    :return:
    """
    zeros_array = np.zeros((2, 2, 2))
    print(f'zeros_array: \n{zeros_array}')
    ones_array = np.ones((2, 2, 2))
    print(f'ones_array: \n{ones_array}')
    # 随件数据，默认float type data占位
    empty_array = np.empty((2, 2, 2))
    print(f'empty_array: \n{empty_array}')


def array_index_iteration():

    array = np.arange(15).reshape(5, 3)
    print(array.shape)
    print(f'array: \n {array}')
    # iteration
    for list in array:
        print(list)
    for data in array.flat:
        print(data)


if __name__ == '__main__':
    array_index_iteration()