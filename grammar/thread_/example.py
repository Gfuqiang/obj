import random
import threading
import time


class Counter:

    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset


def worker(thread_num, run_num, counter):
    time.sleep(random.uniform(0.1, 0.8))
    for _ in range(run_num):
        counter.increment(1)
    print(f'thread {thread_num} complete, {counter.count=}')


def thread_worker_run(func, run_num, counter):
    threads = []
    for i in range(50):
        args = (i, run_num, counter)
        thread = threading.Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    counter = Counter()
    run_num = 10 ** 5
    thread_worker_run(worker, run_num, counter)
    print(f'Should execute time: {run_num * 50}, reality time: {counter.count}')
