
from celery_study.c_demo1 import add
from celery.result import AsyncResult


if __name__ == '__main__':

    # result = add.delay(2, 2)
    res = AsyncResult("1efdda3a-52db-4ba1-")  # 参数为task id
    print(res)
