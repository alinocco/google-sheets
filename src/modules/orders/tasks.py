from celery import shared_task


@shared_task
def add():
    print('Hi, it is my first scheduled task!')
