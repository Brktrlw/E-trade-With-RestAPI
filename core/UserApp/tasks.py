from __future__ import absolute_import, unicode_literals

from celery.task import task

@task(name="deleteOrder")
def add(x, y):
    print(x,y)
    return x * y

