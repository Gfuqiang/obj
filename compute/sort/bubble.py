data_list = [2, 3, 5, 7, 11, 3, 2, 1, 0]


def main(data_list: list):
    for i in range(len(data_list) -1, 0, -1):   # 循环len（）- 1次
        for j in range(i):  # 每次循环找出最大的元素，每次循环元素个数都减一个
            if data_list[j] > data_list[j + 1]:     # 比较两个元素，如果大就交换位置
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
    return data_list


if __name__ == '__main__':
    data_list = main(data_list)
    print(data_list)