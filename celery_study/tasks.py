# from __future__ import absolute_import, unicode_literals
from celery_study.celery import app

@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)


if __name__ == '__main__':
    add.delay(2, 2)