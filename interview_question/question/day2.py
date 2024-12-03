"""
小胖有 n 枚糖，其中第 i 枚糖的类型为 candyType[i] 。小胖注意到她的体重正在增长，所以前去拜访了一位医生。

医生建议 小胖要少摄入糖分，只吃掉她所有糖的 n / 2 即可（n 是一个偶数）。小胖非常喜欢这些糖，她想要在遵循医生建议的情况下，尽可能吃到最多不同种类的糖。

给你一个长度为 n 的整数数组 candyType ，返回： 小胖 在仅吃掉 n / 2 枚糖的情况下，可以吃到糖的 最多 种类数。
"""


def get_candy_type(candy_list):

    if len(candy_list) == 0:
        return 0

    if len(candy_list) % 2 != 0:
        raise Exception('parameter error')

    candy_type_dict = {}
    for candy in candy_list:
        if candy in candy_type_dict:
            candy_type_dict[candy] += 1
        else:
            candy_type_dict[candy] = 0

    eat_candy_num = len(candy_list) / 2
    if len(candy_type_dict.keys()) >= eat_candy_num:
        return int(eat_candy_num)
    else:
        return len(candy_type_dict.keys())


def get_candy_simple(candy_list):

    eat_candy_num = int(len(candy_list) / 2)
    candy_type_num = len(set(candy_list))

    # if eat_candy_num <= candy_type_num:
    #     return eat_candy_num
    # else:
    #     return candy_type_num
    # 上边这段逻辑就是在获取最小值
    return min(eat_candy_num, candy_type_num)


if __name__ == '__main__':
    # 相同的糖果为同一种类型
    candytype = [1, 1, 2, 3, 1, 5, 7, 7, 8, 7]
    ret = get_candy_type(candytype)
    print(ret)
    simple_ret = get_candy_simple(candytype)
    print(ret)