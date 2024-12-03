def first_meth(str1):
    str1 = str1[::-1]
    print(str1)


def get_array_integers(integer):
    init_list = [2, 3, 5, 4, 6, 7, 8]
    for i in range(len(init_list) - 1):
        for j in range(i + 1, len(init_list) - 1):
            if init_list[i] + init_list[j] == integer:
                return (init_list[i], init_list[j])
    return None


def sort_func():
    alist = [{"name": "a", "age": 20}, {"name": "b", "age": 30}, {"name": "c", "age": 25}]
    print(sorted(alist, key=lambda x: x.get('age'), reverse=True))


def delete_list_repeat_element(list_data):
    from collections import Counter
    counter = Counter(list_data)
    for item in counter:
        if counter[item] > 1:
            for _ in range(counter[item]):
                list_data.remove(item)
    print(list_data)


def handle_list(list_data):
    # 讲奇数倒序在前边，偶数正序在后边
    odd_list = []
    even_list = []
    for item in list_data:
        if item % 2 == 0:
            even_list.append(item)
        else:
            odd_list.append(item)
    odd_list.sort(reverse=True)
    even_list.sort()
    odd_list.extend(even_list)
    print(odd_list)


def main():
    str1 = 'abc'
    # first_meth(str1)

    # ret = get_array_integers(7)
    # print(ret)

    # sort_func()

    list_data = [1, 1, 2, 3, 4, 5, 6, 7, 5, 7]
    # delete_list_repeat_element(list_data)
    handle_list(list_data)


if __name__ == '__main__':
    main()