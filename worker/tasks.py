from __future__ import absolute_import

from celery import shared_task


@shared_task
def add(x, y):
    print('Adding %d and %d' % (x,y))
    return x + y


@shared_task
def mul(x, y):
    print('Multiplying %d and %d' % (x,y))
    return x * y


@shared_task
def xsum(numbers):
    print('Summing numbers')
    return sum(numbers)