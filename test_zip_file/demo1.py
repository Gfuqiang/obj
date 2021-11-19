import multiprocessing, os, time


def func(x):
    time.sleep(5)
    return x * x


def main():
    with multiprocessing.Pool(processes=4) as pool:
        # print(pool.map(func, range(10)))

        # res = pool.imap_unordered(func, (5,))   # 使用循环获取result
        # print(type(res)),
        # for i in res:
        #     print(i)

        # res = pool.apply_async(os.getpid, ())
        # print(res.get(timeout=1))

        # multiple_result = [pool.apply_async(os.getpid, ()) for i in range(4)]
        # print([res.get(timeout=1) for res in multiple_result])

        # res = pool.apply_async(time.sleep, (20,))
        # try:
        #     res.get(timeout=1)
        # except TimeoutError:
        #     print(f'Timeout Error')
        pass




if __name__ == '__main__':
    main()
