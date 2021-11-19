from celery import Celery

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery('tasks', backend='redis://127.0.0.1:6379/', broker='redis://127.0.0.1:6379/5')

app.conf.update(
    result_expires=60,
    timezone='Asia/Shanghai'
)

import celery
class MyTask(celery.Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))
        print(f'args: {args}\n'
              f'kwargs: {kwargs}\n einfo: {einfo}')


@app.task(base=MyTask, serializer='json', shadow_name='111111111')
def add(x, y):
    # print(self.request)
    # print(self.id)
    try:
        logger.info(f'add function start execute .................')
        return x / y
    except Exception as e:
        raise KeyError(e)


