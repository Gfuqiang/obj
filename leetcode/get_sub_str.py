"""
获取字符串的所有子字符串
"""


s = 'abcd'
# ab,ac,ad,abc,abd,acd
# bc,bd,bcd
# cd


def get_sub_str():
    ret = []
    s = 'abcd'
    for i in range(len(s)):
        ret.append(s[i])
        for second_pointer in range(i + 1, len(s)):
            label = s[i:second_pointer]
            for g in range(second_pointer, len(s)):
                ret.append(label + s[g])
    print(ret)


if __name__ == '__main__':
    get_sub_str()
