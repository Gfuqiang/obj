import multiprocessing
import os


def create_file(content):

    with open('1.txt', 'a') as f:
        f.write("子进程号[%s]拿到文件光标位置>>%s\n" % (os.getppid(), f.tell()))
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
    for result in pool.imap(create_file, ['11111111111111', '222222', '33333', '555555', '666666']):
        print(result)

