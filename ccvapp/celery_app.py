from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from kombu import Exchange, Queue


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ccv.settings')

app = Celery('ccvapp')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
#app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.task_queues = (
    Queue('default',  Exchange('default'),   routing_key='default'),
)
app.conf.task_default_queue = 'default'
app.conf.task_default_exchange_type = 'default'
app.conf.task_default_routing_key = 'default'


