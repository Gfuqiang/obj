from celery import Celery
app = Celery('tasks', backend='redis://172.80.0.7:6379', broker='amqp://guest@172.80.0.8:5672')
@app.task
def add(x, y):
    return x + y