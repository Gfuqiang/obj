"""
读取文件；

去除所有标点符号和换行符，并把所有大写变成小写；

合并相同的词，统计每个词出现的频率，并按照词频从大到小排序；

将结果按行输出到文件out.txt。
"""

import os
import re
from collections import abc
base_path = os.path.dirname(__file__)

input_file_name = 'input_file.txt'
output_file_name = 'output.txt'
file_dir_path = base_path + '/file_dir/'

input_file_path = file_dir_path + input_file_name
output_file_path = file_dir_path + output_file_name

global data_dict
data_dict = {}

punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'
def dispose(file_data):

    print(file_data)
    # 去除标点符号
    file_data = re.sub(r'[^\w ]', ' ', file_data)

    file_data = file_data.lower()

    file_data_list = file_data.split(' ')

    # 去除空白单词
    file_data_list = filter(None, file_data_list)

    # 统计
    statistics(file_data_list)

def statistics(file_data_list):

    for data in file_data_list:
        if data in data_dict:
            data_dict[data] += 1
        else:
            data_dict[data] = 1

def write_file(datas):
    with open(output_file_path, 'w') as e:
        for key in datas:
            e.write(f'{key},{datas[key]}\n')


with open(input_file_path, 'r') as e:
    data = e.read()
    dispose(data)

write_file(data_dict)





