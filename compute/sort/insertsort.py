def insert_sort(list_data):
    # 默认第一个值是最大或者最小。
    for i in range(1, len(list_data)):
        # 获取前一个值index
        pre_index = i - 1
        # 记录循环到的值，拿这个值和前边每一个做比较，大于前边的数就代表是排序结果的位置了，将值放在这里就完成了这个值的排序
        current = list_data[i]
        """
        拿最新值和该值前边每一个值进行比较，
        前一个值大于当前值，将大值放在当前索引位置，索引减一
        前一个值小于当前值时，就将该值放在小于值的后边。
        """
        while pre_index >= 0 and list_data[pre_index] > current:
            list_data[pre_index + 1] = list_data[pre_index]
            pre_index -= 1
        list_data[pre_index + 1] = current
    return list_data