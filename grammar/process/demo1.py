import os
import re
from multiprocessing import Process


def func(file, mode):
    with open(file, mode, encoding="utf-8") as f:
        f.write("子进程号[%s]拿到文件光标位置>>%s\n" % (os.getppid(), f.tell()))


if __name__ == '__main__':
    print("主进程开始.")
    file_name = "filename.txt"
    p_lst = []
    for i in range(10):
        p = Process(target=func, args=(file_name, "a"))
        p.start()
        p_lst.append(p)

    [pp.join() for pp in p_lst]
    # with open(file_name, "r", encoding="utf-8") as f:
    #     data = f.read()
    #     all_num = re.findall('\d+', data)
    #     print("文件[%s]中的数字%s,存在的次数: %s" % (file_name, all_num, len(all_num)))
    print("主进程结束.")