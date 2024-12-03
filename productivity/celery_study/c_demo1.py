import celery

from productivity.celery_study import app, logger


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


if __name__ == '__main__':
    add.delay(2, 2)

