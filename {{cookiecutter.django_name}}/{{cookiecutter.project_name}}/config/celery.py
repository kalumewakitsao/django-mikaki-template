import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ cookiecutter.project_name }}.config.settings')

app = Celery('{{ cookiecutter.project_name }}')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sample_periodic_task': {
        'task': '{{ cookiecutter.project_name }}.app1.tasks.sample_task',
        'schedule': 30.0,
        'args': ()
    },
}
app.conf.timezone = 'UTC'
