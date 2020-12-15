import threading
import time


def test1():
    time.sleep(1)
    print(f'function run: {test1.__name__}')


def test2():
    time.sleep(5)
    print(f'function run: {test2.__name__}')


def main():
    print(f'thread num: {threading.enumerate()}')
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    t2.start()

    while True:
        thread_num = len(threading.enumerate())
        print(f'线程数量是：{thread_num}')
        if thread_num <= 1:
            break
        time.sleep(1)


if __name__ == '__main__':
    main()