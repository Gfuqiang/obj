def quick_sort(data_list, start, end):

    if start >= end:
        return

    l_index = start
    r_index = end

    mid = data_list[start]
    while l_index < r_index:
        while data_list[r_index] >= mid and l_index < r_index:
            r_index -= 1
        data_list[l_index] = data_list[r_index]
        while data_list[l_index] <= mid and l_index < r_index:
            l_index += 1
        data_list[r_index] = data_list[l_index]

    data_list[l_index] = mid

    quick_sort(data_list, start, l_index - 1)
    quick_sort(data_list, l_index + 1, end)

    return data_list


def marge_sort(data_list):

    if len(data_list) <= 1:
        return data_list

    mid = len(data_list) // 2
    left_list = marge_sort(data_list[:mid])
    right_list = marge_sort(data_list[mid:])

    return marge_list(left_list, right_list)


def marge_list(left, right):

    new_list = []

    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            new_list.append(left[l])
            l += 1
        else:
            new_list.append(right[r])
            r += 1

    if l == len(left):
        new_list.extend(right[r:])
    else:
        new_list.extend(left[l:])

    return new_list


def bubble_sort(data_list):
    for i in range(len(data_list) - 1, 0, -1):
        for j in range(i):
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
    return data_list


def insert_sort(data_list):
    """
    思路
        1. for 循环从列表中取出数据，从index 1开始取，current元素，因为要和前一个元素进行比较
        2. 将current的前边元素依次取出，如果大于current，代表current小要放在前边，将当前比较元素后移一位。（注意取前边元素要判断索引不能
        小于0），如果前边的元素小于current了，就将current放在当前位置就完成了排序。

    """
    for index in range(1, len(data_list)):

        prev = index - 1
        current = data_list[index]

        while prev >= 0 and data_list[prev] > current:
            data_list[prev + 1] = data_list[prev]
            prev -= 1
        data_list[prev + 1] = current

    return data_list


def count_sort(list_data):
    """
    计数排序，不适合最大值和最小值差距太大时使用，因为存储计数的列表会有很多用不到。
    """

    ret_list = []
    max_data = max(list_data)
    min_data = min(list_data)
    # 确定用于计数的容器长度
    k = (max_data - min_data) + 1
    # 偏移值，用来计算放在计数容器中的位置。
    offset = min_data
    list_container = [0] * k

    for data in list_data:
        if list_container[data - offset] != 0:
            list_container[data - offset] += 1
        else:
            list_container[data - offset] = 1

    for i in range(len(list_container)):
        if list_container[i] != 0:
            while list_container[i] > 0:
                ret_list.append(i + min_data)
                list_container[i] -= 1

    return ret_list


if __name__ == '__main__':
    data_list = [3, 9, 3, 2, 11, 4, 5, 6, 7, 10]
    # ret = quick_sort(data_list, 0, len(data_list) - 1)
    # ret = marge_sort(data_list)
    # ret = bubble_sort(data_list)
    ret = insert_sort(data_list)
    print(ret)