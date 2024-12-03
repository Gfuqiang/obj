"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
"""
from functools import reduce

map_dict = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def get_word_grop(str_data):

    if len(str_data) == 0:
        return []

    if len(str_data) == 1:
        return map_dict[str_data]

    if len(str_data) >= 2:
        one = [w for w in map_dict[str_data[0]]]
        second = [w for w in map_dict[str_data[1]]]
        ret = marge_list(one, second)
        for i in range(2, len(str_data)):
            ret = marge_list(ret, map_dict[str_data[i]])
        return ret

    # new_list = []
    # for index, num in enumerate(str_data):
    #     word_list = [w for w in map_dict[num]]
    #     new_list.append(word_list)
    #
    # return my_reduce(marge_list, new_list)


def my_reduce(func, iterator):

    ret = func(iterator[0], iterator[1])
    for index in range(2, len(iterator)):
        ret = func(ret, iterator[index])
    return ret


def marge_list(one, second):

    ret = []
    if not second:
        return one
    for i in one:
        for j in second:
            ret.append(f'{i}{j}')
    return ret


def quick_sort(data_list, start, end):

    if start >= end:
        return

    l_index = start
    r_index = end

    mid_data = data_list[start]
    while l_index < r_index:
        while data_list[r_index] >= mid_data and l_index < r_index:
            r_index -= 1
        data_list[l_index] = data_list[r_index]
        while data_list[l_index] <= mid_data and l_index < r_index:
            l_index += 1
        data_list[r_index] = data_list[l_index]

    data_list[l_index] = mid_data

    quick_sort(data_list, start, l_index - 1)
    quick_sort(data_list, l_index + 1, end)

    return data_list


if __name__ == '__main__':

    # ret = get_word_grop('234')
    # print(ret)

    data_list = [3, 4, 5, 7, 9, 10, 12, 1, 1]
    ret = quick_sort(data_list, 0, len(data_list) - 1)
    print(ret)