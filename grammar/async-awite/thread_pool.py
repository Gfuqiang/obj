from concurrent.futures import ThreadPoolExecutor, wait
import time
import threading


def demo(a, b):
    time.sleep(a)
    print(threading.current_thread())
    return a + b


def main():
    executor = ThreadPoolExecutor(max_workers=2)

    # task1 = executor.submit(demo, 2, 3)
    # task2 = executor.submit(demo, 3, 5)
    # print(task1.result())
    # print(task2.result())

    # 阻塞主线程，等待任务执行完，可通过参数控制都执行完成还是部分执行完成。
    # all_task = [executor.submit(demo, a, b) for a, b in [(2, 3), (1, 2)]]
    # wait(all_task)
    # print(1)

    # 和submit不同 不是先完成就返回结果。结果的打印顺序和参数传递顺序相同。
    tasks = executor.map(demo, [3, 2], [3, 1])
    print(threading.enumerate())
    for task in tasks:
        print(task)



if __name__ == '__main__':
    main()