import math
import os
import random, datetime

import numpy as np

# x = 0
# while x != 209:
#     x = np.random.randint(1, 209, size=(50,))
#     x = sum(x)
# print(x)


def sample_random_list(sample_max, summation, sample_num):

    random_list = random.sample(range(1, sample_max), k=sample_num - 1)
    print(random_list)
    ratio = summation / sum(random_list)
    ret = [1 if math.floor(data * ratio) <= 0 else math.floor(data * ratio) for data in random_list]
    print(f"ret: {ret}")
    print(sum(ret))
    ret.append(summation - sum(ret))
    print(sum(ret))


def is_dir():
    dir = os.listdir('../demo')
    for file in dir:
        if os.path.isdir(file):

            print(file)


if __name__ == '__main__':
    is_dir()

