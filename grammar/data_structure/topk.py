"""
使用堆解决topk问题，找到一组数据中最大的k个值
用堆实现好处，内存使用总是堆得大小，对限制内存使用很适用。
"""

import heapq
import random


class TopK:

    def __init__(self, k, iterable):
        self.min_heap = []
        self.capacity = k
        self.iterable = iterable

    def push(self, val):
        if len(self.min_heap) > self.capacity:  # 判断堆容量是否达到k个
            min_data = self.min_heap[0]     # 最小堆，堆顶数据最小
            if min_data < val:
                heapq.heapreplace(self.min_heap, val)   # 将val值放入，并重置堆
        else:
            heapq.heappush(self.min_heap, val)  # 向堆中添加数据

    def get_topk_value(self):
        for i in self.iterable:
            self.push(i)
        return self.min_heap


if __name__ == '__main__':
    iterable = [i for i in range(1000)]
    random.shuffle(iterable)
    print(iterable)
    top_k = TopK(9, iterable)
    ret = top_k.get_topk_value()
    print(ret)

