def delete_repetition_element():
    # 删除列表中重复元素

    list_data = ['a', 'b', 'c', 'a', 'b']

    print('first')
    print(sorted(set(list_data), key=list_data.index))
    print('second')
    new_list_data = []
    for data in list_data:
        if data not in new_list_data:
            new_list_data.append(data)
    print(new_list_data)


def get_diffrent_item():
    # 找出列表中相同和不同的元素

    l1 = [1, 2, 3]
    l2 = [3, 5, 4]
    set1 = set(l1)
    set2 = set(l2)
    print(set1 & set2)
    print(set1 ^ set2)


def delete_list_element_not_create_new_list():

    # 遍历列表时删除元素

    l1 = [1, 2, 3, 4]
    print(id(l1))
    print(id(l1[:]))
    for i in l1[:]:
        if i > 2:
            l1.remove(i)
    print(l1)

    # 倒序遍历，即使删除元素，没有遍历到的元素索引也不会变
    l2 = [1, 2, 3, 4]
    for i in range(len(l2) - 1, -1, -1):
        if l2[i] > 2:
            l2.remove(l2[i])
    print(l2)


def main():
    # delete_repetition_element()
    # get_diffrent_item()
    delete_list_element_not_create_new_list()


if __name__ == '__main__':
    main()