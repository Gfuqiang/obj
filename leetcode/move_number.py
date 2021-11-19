"""
将列表中0元素移动到列表末尾，其他元素顺序不变
"""


def mv_zero(data_list):
    for i in data_list:
        if i == 0:
            data_list.remove(i)
            data_list.append(0)
        print(len(data_list))
    return data_list


def mv_zero_func1(data_list):
    # 元素交换
    k = 0
    for index in range(len(data_list)):
        if data_list[index] != 0:
            if k != index:
                data_list[k], data_list[index] = data_list[index], data_list[k]
                k += 1
            else:
                k += 1
    return data_list


if __name__ == '__main__':
    data_list = [8, 2, 3, 0, 1, 5, 6, 0]
    # data_list = (i for i in range(0, 10))
    # data_list = mv_zero(data_list)
    data_list = mv_zero_func1(data_list)
    print(data_list)