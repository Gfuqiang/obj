from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('celery_study',
             broker='amqp://172.80.0.8:5672',
             backend='amqp://172.80.0.8:5672',
             include=['celery_study.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.worker_main()