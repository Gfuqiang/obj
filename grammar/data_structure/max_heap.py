"""
实现最大堆
堆总是一个完全二叉树，优先队列是以堆得方式实现的。
堆的数据以广度优先方式放入数组中，父子节点对应到数组中index是有规律的。
以根节点对应数组中索引为0为例，规律是 父节点index * 2 + 1 == 左节点index， 父节点index * 2 + 2 == 右节点index
"""

import math


class MaxHeap:

    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, val):
        self.heap.append(val)
        index = len(self.heap) - 1
        while True:
            father_index = math.floor((index - 1)/2)
            # 不是根节点，且大于父节点值，对调父子节点值
            if index > 0 and self.heap[index] > self.heap[father_index]:
                # 子节点和父节点对调位置
                self.heap[index], self.heap[father_index] = self.heap[father_index], self.heap[index]
                index = father_index
            else:
                return

    def __call__(self, *args, **kwargs):
        print(self.heap)


if __name__ == '__main__':
    max_heap = MaxHeap()
    max_heap.insert(3)
    max_heap.insert(4)
    max_heap.insert(2)
    max_heap.insert(10)
    max_heap.insert(8)
    max_heap.insert(3)
    max_heap.insert(1)

    print(max_heap.size())
    max_heap()

