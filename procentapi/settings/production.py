
# production but not under development
import os

from procentapi.settings.base import BASE_DIR
from . base import *
import django_heroku

DEBUG = False
ALLOWED_HOSTS = ['peaceful-badlands-38433-2cbf049590ab.herokuapp.com', '0.0.0.0']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
REDIS_HOST = 'ec2-52-70-18-167.compute-1.amazonaws.com'
REDIS_PORT = '23940'
REDIS_DB = 1

# # Celery Configuration docker
CELERY_BROKER_URL = 'amqps://mnblvtxv:Sn6DfuO620YOAZ3eikewGOn4mycnV1yz@fish.rmq.cloudamqp.com/mnblvtxv'
CELERY_RESULT_BACKEND = 'redis://ec2-52-70-18-167.compute-1.amazonaws.com:23940/1'

django_heroku.settings(locals(), test_runner=False)