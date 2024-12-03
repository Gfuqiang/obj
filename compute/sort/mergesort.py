"""
归并排序：
    分治思想
    https://mp.weixin.qq.com/s/YY63D6ZkC4Jhon2H6-ZAKw
    https://www.cnblogs.com/shierlou-123/p/11310040.html
"""


def merge_sor(list_data: list) -> list:
    # 将列表拆分为只有一个元素
    if len(list_data) <= 1:
        return list_data
    meddle = len(list_data) // 2
    # 这里递归将列表一分为2，直到无法继续分割
    left_list = merge_sor(list_data[:meddle])
    right_list = merge_sor(list_data[meddle:])
    return merge_list(left_list, right_list)


def merge_list(left_list, right_list):
    """
    疑问： 该方法传入两个数组不能合并成有序的新数组嘛？ 不能 [5, 2], [4, 1],该方法合并完是[4, 1, 2, 5]. 该方法合并两个有序的数组
    新数组才是有序的。或者合并两个一个元素的数组，归并排序就是这样，将单个元素的数组合并后变为有序，在讲有序的数组进行合并。
    """
    result_list = []
    j = h = 0
    # 判断索引不能越界
    while j < len(left_list) and h < len(right_list):
        if left_list[j] < right_list[h]:
            result_list.append(left_list[j])
            j += 1
        else:
            result_list.append(right_list[h])
            h += 1

    # 判断其中一个列表为空时，将另一列表中元素全部加入新列表
    if len(left_list) == j:
        result_list.extend(right_list[h:])
    else:
        result_list.extend(left_list[j:])

    return result_list


if __name__ == '__main__':
    list_data = [1, 3, 7, 4, 2, 8, 9]
    result_list = merge_sor(list_data)
    print(result_list)