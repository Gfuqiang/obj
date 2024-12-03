"""
celry 结构化启动服务文档：https://docs.celeryq.dev/en/stable/getting-started/next-steps.html#project-layout

运行celery worker 进入 productivity，执行：celery -A celery_study worker --loglevel=INFO
"""
from celery import Celery

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

REDIS_IP = '10.100.7.2'

backend = f'redis://{REDIS_IP}:6398/6'
broker = f'redis://{REDIS_IP}:6398/5'

app = Celery('celery_study', backend=backend, broker=broker)

app.conf.update(
    result_expires=60,
    timezone='Asia/Shanghai'
)

if __name__ == '__main__':
    app.start()