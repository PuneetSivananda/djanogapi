import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproj.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
from celery import Celery

app = Celery('tasks', broker="amqp://localhost//")

@app.task
def reverse(string):
  return string[::-1]

#rabbitmq-server.bat restart
#rabbitmq-server.bat status
#celery -A tasks worker --loglevek=info