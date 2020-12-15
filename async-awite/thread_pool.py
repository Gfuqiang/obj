from concurrent.futures import ThreadPoolExecutor
import time


def demo(a, b):
    time.sleep(a)
    return a + b


def main():
    executor = ThreadPoolExecutor(max_workers=2)
    task1 = executor.submit(demo, 2, 3)
    task2 = executor.submit(demo, 3, 5)
    print(task1.result())
    print(task2.result())


if __name__ == '__main__':
    main()