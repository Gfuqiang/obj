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