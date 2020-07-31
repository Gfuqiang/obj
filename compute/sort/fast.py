

def fast_sort(data_list):

    for i in range(len(data_list)-1, -1, -1):
        max_data = data_list[i]
        max_index = i
        for j in range(i - 1, -1, -1):
            if data_list[j] > data_list[max_index]:
                max_data = data_list[j]
                max_index = j
        data_list[max_index], data_list[i] = data_list[i], data_list[max_index]
    return data_list
if __name__ == '__main__':
    # print(list(i for i in range(10, -1, -1)))
    data_list = [2, 3, 5, 7, 11, 3, 2, 1, 0]
    print(fast_sort(data_list))

