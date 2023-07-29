from dotenv import dotenv_values
from celery import Celery


config  = {
    **dotenv_values('.env')
}

background = Celery('tasks', broker_url=f"{config['QUEUE']}://{config['QUEUE_HOST']}:{config['QUEUE_PORT']}/{config['QUEUE_NAME']}")
