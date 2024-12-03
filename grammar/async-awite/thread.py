import random
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# 创建线程锁
print_lock = threading.Lock()

def print_content(content):
    with print_lock:
        print(content)

def thread_instance():
    # 创建多个线程并启动
    threads = []
    for i in range(5):
        t = threading.Thread(target=print_content, args=(f"Thread {i+1}: Hello, World!",))
        threads.append(t)
        t.start()

    # 等待所有线程结束
    for t in threads:
        t.join()


def thread_pool():
    with ThreadPoolExecutor() as executor:
        task_list = []
        for i in range(5):
            task_list.append(executor.submit(print_content, f"Thread {i+1}: Hello, World!"))
        for task in as_completed(task_list):
            ...


if __name__ == '__main__':
    thread_pool()

