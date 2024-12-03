"""
小内存读取大文件问题
"""
import os, math
from get_statistic_fiel import get_file_path
from mmap import mmap

p = get_file_path('big_file_test.txt')


def main():
    # i = []
    with open(p, 'r+') as f:
        m = mmap(f.fileno(), 0)
        temp = 0
        for index, data in enumerate(m):
            if data == b'\n':
                yield m[temp: index + 1].decode()
                temp = index + 1


def test_file_len_function():
    with open(p, 'rb') as f:
        file_len = os.path.getsize(p)
        read_time = math.ceil(file_len / 3)
        print(read_time)
        for count in range(1, read_time):
            data = f.read(3)
            yield data


if __name__ == '__main__':
    for data in test_file_len_function():
        print(data)