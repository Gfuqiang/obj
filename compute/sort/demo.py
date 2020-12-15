def main(list_data):
    if len(list_data) < 2:
        return list_data
    middle = len(list_data) // 2
    left_list_data = main(list_data[:middle])
    right_list_data = main(list_data[middle:])
    new_list_data = merge_list(left_list_data, right_list_data)
    return new_list_data


def merge_list(left_list_data, right_list_data):
    new_list_data = []
    h = j = 0
    while True:
        if left_list_data[h] < right_list_data[j]:
            new_list_data.append(left_list_data[h])
            h += 1
        else:
            new_list_data.append(right_list_data[j])
            j += 1

        if len(left_list_data) == h:
            new_list_data.extend(right_list_data[j:])
            break
        if len(right_list_data) == j:
            new_list_data.extend(left_list_data[h:])
            break
    return new_list_data


def insert_sort(list_data):
    for i in range(1, len(list_data)):
        # 获取前一个值index
        pre_index = i - 1
        # 记录循环出来的最新值
        current = list_data[i]
        # 拿最新值和前边一个值进行比较，
        """
        1. 比前一个值大：直接放在前一个值后边也就是index为pre_index这个值后面
        2. 比前一个值小：将前一个值向后移动一位，继续获取前一个值进行比较
        """
        while pre_index >= 0 and list_data[pre_index] > current:
            list_data[pre_index + 1] = list_data[pre_index]
            pre_index -= 1
        # 比前一个值大，放在前一个值后边
        list_data[pre_index + 1] = current
    return list_data


if __name__ == '__main__':
    list_data = [1, 2, 5, 6, 9, 3, 1]
    new_data = main(list_data)
    print(new_data)

    new_data = insert_sort(list_data)
    print(new_data)

