from tool import watch
"""
二分查找：
    两种问法(区别在于是否获取index)
    1. 找到target 在列表中的index
    2. 查找target是否在列表中
"""


@watch.func_time_watch
def create_ordered_list():
    list_data = []
    for i in range(20):
        list_data.append(i)
    return list_data


def binary_search_func(list_data, target):
    # 1，2问法都可以实现
    l_index = 0
    r_index = len(list_data) - 1
    while l_index <= r_index:
        middle_index = (l_index + r_index) // 2
        if list_data[middle_index] == target:
            return middle_index
        if target < list_data[middle_index]:
            r_index = middle_index - 1
        else:
            l_index = middle_index + 1
    return -1


def binary_search_recursion_func(r, l, target, data_list):
    # 1，2问法都可以实现
    if r == l:
        if target == data_list[r]:
            return r
        else:
            return -1
    else:
        middle_index = (r + l) // 2
        if target == data_list[middle_index]:
            return middle_index
        if target < data_list[middle_index]:
            return binary_search_recursion_func(r, middle_index - 1, target, data_list)
        else:
            return binary_search_recursion_func(middle_index + 1, l, target, data_list)


def binary_search_recursion_func1(target, data_list):
    # 只能实现2的问法

    # 这里判断0的意义 a =【1，2，3】 a[1:1] [],长度为0 就代表截取字符串传入的index相同。
    if len(data_list) == 0:
        return False
    middle = len(data_list) // 2
    if target == data_list[middle]:
        return True
    if target < data_list[middle]:
        return binary_search_recursion_func1(target, data_list[:middle])
    else:
        return binary_search_recursion_func1(target, data_list[middle + 1:])


if __name__ == '__main__':
    list_data = create_ordered_list()
    # target_index = binary_search_func(list_data, 10)
    # target_index = binary_search_recursion_func(0, len(list_data) - 1, 6, list_data)
    target_index = binary_search_recursion_func1(31, list_data)
    print(target_index)
