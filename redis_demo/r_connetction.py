import redis

r = redis.Redis(decode_responses=True)
r.set('key', 'val', 60)
# r.delete('key')
# print(r.get('key'))

# 添加zset数据
# r.zadd('zset', {"one": 4, "tow": 5, "three": 3})
# 获取zset数据，添加开始索引和结束索引
# print(r.zrange('zset', 0, -1))

# hash
# r.hset('hash', 'name', 'zhang san')

# list
# r.lpush('list_k', 'list_v')
r.linsert('list_k', 'before', 'list_v', 'list_v_b')