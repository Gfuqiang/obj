from operator import itemgetter

a = [
    [1, 1, 2, 21, 2],
    [1, 10, 2, 10, 2],
    [1, 2, 2, 8, 1],
    [1, 1, 3, 9, 1],
    [2, 1, 1, 1, 1],
    [1, 1, 4, 1, 1]
]


import re

picture_name_list = ["(flow_3)_(3_4)ocr_0.134383.png",
                     "(flow_1)_(3_10)ocr_0.23483.png",
                     "(flow_2)_(3_4)ocr_0.13283.png",
                     "(flow_1)_(inner_3)_(3_3)ocr-0.13483.png",
                     "(flow_1)_(3_2)ocr_0.53483.png"]


def sort_picture(name):
    if "inner" in name:
        res = re.search("\(flow_(.*)\)_\(inner_(.*)\)_\((.*)_(.*)\).*", name)
        compare = (res.group(1), res.group(2), "1", res.group(3), res.group(4))
    else:
        res = re.search("\(flow_(.*)\)_\((.*)_(.*)\).*", name)
        compare = (res.group(1), res.group(2), res.group(3), "1", "1")
    print(compare)
    return compare




if __name__ == '__main__':
    # b = sorted(a, key=itemgetter(1, 2, 3, 4))
    # print(b)

    res = sorted(picture_name_list, key=sort_picture)
    print(res)
