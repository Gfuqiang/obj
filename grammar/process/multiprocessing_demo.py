import multiprocessing
import time


def get_html(n):
    print(f'start get html')
    time.sleep(n)
    return n


def get_url(n):
    print(f'start get url')
    time.sleep(n)
    return n


def get_fiel(n):
    print(f'start get file')
    time.sleep(n)
    return n


if __name__ == '__main__':
    # 创建进程执行函数
    # process = multiprocessing.Process(target=get_html, args=(2,))
    # process1 = multiprocessing.Process(target=get_html, args=(5,))
    # print(process.pid)
    # print(f'process1: {process1.pid}')
    # process.start()
    # process1.start()
    # print(process.pid)
    # print(f'process1: {process1.pid}')
    # print(f'process1: {process1.is_alive()}')
    # process.join()
    # process1.join()
    # print(f'process run end')

    # 进程池
    print(multiprocessing.cpu_count())
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(2,))
    # result1 = pool.apply_async(get_url, args=(2,))
    # result2 = pool.apply_async(get_fiel, args=(2,))
    # 关闭pool，运行过程中不允许新的任务添加
    # pool.close()
    # pool.join()
    # print(result.get())
    # print(result1.get())
    # print(result2.get())

    # join,start,close, get获取结果等方法做的事情。imap和imap_unordered进行了封装，不需要在去单独调动

    # imap 根据传参顺序执行，并返回结果
    # for result in pool.imap(get_html, [1, 5, 3]):
    #     print(result)

    # imap_unordered 执行快的先返回结果
    for result in pool.imap_unordered(get_html, [1, 5, 3]):
        print(result)
