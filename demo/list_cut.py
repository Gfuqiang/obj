from collections import Counter
import numpy as np
import math


def statistics_number_range(sample_data_list: list):
    sample_data_list.sort()
    result_list = []
    for data in sample_data_list:
        int_data = data * 100
        first_num = int_data // 10
        last_num = data % 10
        if last_num <= 5 and last_num >=0:
            max_range = (first_num + 1) * 10 - 5
            min_range = first_num * 10
        else:
            min_range = first_num * 10 + 6
            max_range = (first_num + 1) * 10
        result_list.append(f'{round(min_range / 100, 2)}-{round(max_range / 100, 2)}')
    return dict(Counter(result_list))



def demo_two(sample_data_list):
    results = {}
    # 校验数据保留3位小数
    sample_data_list = [round(i, 3) for i in sample_data_list if i > 0]
    # 处理 list 长度为0 或 1
    if len(sample_data_list) == 0:
        return results
    elif len(sample_data_list) == 1:
        value = sample_data_list[0]
        results[f'{value}-{value}'] = 1
        return results
    sample_data_list.sort()
    # 最大值减最小值 平分为5份
    max_data = max(sample_data_list)
    print(max_data)
    min_data = min(sample_data_list)
    print(min_data)
    temp_data = round((max_data - min_data) / 5, 3)
    print(temp_data)
    # 获取每份节点值
    template = [round(i, 3) for i in np.arange(min_data, max_data, temp_data)]
    template[len(template) - 1] = max_data
    print(template)
    # 生成x轴数据
    for i in range(len(template)):
        if i == len(template) - 1:
            break
        key = f'{template[i]}-{template[i + 1]}'
        results[key] = 0
    for data in sample_data_list:
        # 计算比最小值大多少份，向上取整
        location = math.ceil((data - min_data) / temp_data)
        if location == 0:
            location = 1
        if location > len(template) - 1:
            location = len(template) - 1
        key = f'{template[location - 1]}-{template[location]}'
        if key in results:
            results[key] += 1
        else:
            results[key] = 1
    print(results)
    return results


if __name__ == '__main__':
    # result = demo_two(data)
    # print(result)
    data = [
        0.2667,
        0.2917,
        0.3333,
        0.35,
        0.3167,
        0.2417,
        0.2583,
        0.3083,
        0.2333,
        0.2833,
        0.3167,
        0.275,
        0.3,
        0.275,
        0.2583,
        0.3417,
        0.2417,
        0.3,
        0.2917,
        0.3417,
        0.3417,
        0.3417
    ]
    data1 = [0.4123]
    # result = demo_two(data)
    # print(result)
    import pandas as pd
    #
    # data = [round(i, 3) for i in data if i > 0]
    print(len(data))
    print(max(data))
    print(min(data))
    categories = pd.qcut(data, 4, duplicates='drop', retbins=True)
    print(categories)
    for interval, count in categories.value_counts().items():
        # 左边界 右边界  数量
        print(interval.left, interval.right, count)

    # categories = pd.cut(data, 5)
    # print(categories)
    # print(dir(categories))
    print('*' * 30)
    data = math.ceil(1000 * 0.2456) / 1000
    data1 = math.floor(1000 * 0.2450) / 1000
    print(data)
    print(data1)
