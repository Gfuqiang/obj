import multiprocessing
import os, time
import random


def create_file(content):
    print(os.getpid())
    sleep_time = random.randint(5, 10)
    print(sleep_time)
    time.sleep(sleep_time)
    with open('1.txt', 'a') as f:
        f.write("子进程号[%s]拿到文件光标位置>>%s\n" % (os.getpid(), f.tell()))
    return content


if __name__ == '__main__':

    # print(f'start create main')
    # process_list = []
    #
    # for i in range(5):
    #     process = multiprocessing.Process(target=create_file)
    #     process.start()
    #     print(os.getpid())
    #     process_list.append(process)
    #     process.join()
    #
    # # [process.join() for process in process_list]
    # print(f'main the end')
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    list_data = [(i, i+1) for i in range(10)]
    print(list_data)
    for result in pool.imap_unordered(create_file, list_data):
        pass
    time.sleep(1)
    print('*' * 10)
    time.sleep(1)
    print('*' * 10)
    time.sleep(1)
    print('*' * 10)
    time.sleep(1)
    print('*' * 10)
    time.sleep(1)
    print('*' * 10)

