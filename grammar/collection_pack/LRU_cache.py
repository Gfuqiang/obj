"""
实现一个LRUCache
缓存策略，将最不常用的数据移除，以达到释放内存的目的
"""

import collections


class LRUCache:
    """
    每次获取或添加数据，将视为常用数据放在头部
    """

    def __init__(self, capacity):
        self.dd = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.dd:
            value = self.dd[key]
            self.dd.move_to_end(key)
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.dd:
            del self.dd[key]
            self.dd[key] = value
        else:
            self.dd[key] = value
            if len(self.dd) > self.capacity:
                self.dd.popitem(last=False)


if __name__ == '__main__':
    lru_cache = LRUCache(3)
    for i in range(3):
       lru_cache.put(i, i)
    lru_cache.put('a', 1)
    print(lru_cache.dd)
    assert len(lru_cache.dd) <= 3, "gt capacity"


