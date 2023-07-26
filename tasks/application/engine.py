from celery import Celery
from dotenv import dotenv_values

config  = {
    **dotenv_values('.env')
}

background = Celery('tasks', broker_url=f"{config['QUEUE']}://:{config['QUEUE_PASSWORD']}@{config['QUEUE_HOST']}:{config['QUEUE_PORT']}/0")
