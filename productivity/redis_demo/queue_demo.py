import datetime
import pickle

import redis, threading
import queue
from collections import deque


class MyQueue:

    def __init__(self):
        self.queue = deque()

    def append(self, val):
        self.queue.append(val)


def update_redis_val(r, key, val):
    try:
        r.set(key, val, ex=300)
    except Exception as e:
        print(f'update_redis_val error info: {e}')


def pipe_update_redis_data(pipe):
    pipe.multi()
    pipe.set('watch_key', 'watch_val_3', ex=300)
    pipe.get('watch_key')


if __name__ == '__main__':
    # dq = deque()
    # dq.append({"a": 1})
    # # dq.append(2)
    # # dq.appendleft(3)
    # # dq.appendleft(4)
    # # print(dq.index(1))
    # # dq.insert(2, 5)
    # print(dq)
    """
    my_queue = MyQueue()
    data1 = {
            'jobs': [{'job': 1, 'first_execute': True}],
            "execute": True, "tboard": "sub_t1", 'start_time': datetime.datetime.now(),
            'process_time': 300
        }
    data2 = {
            'jobs': [{'job': 2, 'first_execute': True}],
            "execute": False, "tboard": "sub_t2", 'start_time': datetime.datetime.now(),
            'process_time': 400
        }
    data3 = {
        'jobs': [{'job': 3, 'first_execute': True}],
        "execute": False, "tboard": "sub_t2", 'start_time': datetime.datetime.now(),
        'process_time': 300
    }
    my_queue.append(data1)
    my_queue.append(data2)
    r = redis.Redis()
    r.set('device_1', pickle.dumps(my_queue), ex=600)
    my_queue = pickle.loads(r.get('device_1'))
    data2_index = my_queue.queue.index(data2)
    my_queue.queue.insert(data2_index, data3)
    my_queue.queue.rotate()
    print(my_queue.queue[1])
    print(f"data2_index: {data2_index}")
    """
    r = redis.Redis()
    r.set('watch_key', 'watch_val_1', ex=300)
    """
    乐观锁使用流程：
    1. 获取管道符    r.pipeline()
    2. 获取watch      watch = pipe.watch('watch_key')
    3. 开启事务     pipe.multi()
    4. set 更新数据     pipe.set('watch_key', 'watch_val_3', ex=300)， 更新失败会报错
    transaction 封装了对watch的获取，提供更新数据函数即可
    """
    pipe = r.pipeline()
    watch = pipe.watch('watch_key')
    print(f'watch: {watch}')
    # t1 = threading.Thread(target=update_redis_val, args=(r, 'watch_key', 'watch_val_2'))
    # t1.start()
    print(r.get('watch_key'))
    # t1.join()
    # pipe.multi()
    # pipe.set('watch_key', 'watch_val_3', ex=300)
    # pipe.get('watch_key')
    # print(pipe.execute())
    res = r.transaction(pipe_update_redis_data, 'watch_key')
    print(f'transaction result:{res}')






