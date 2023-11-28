
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
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']
REDIS_DB = os.environ['REDIS_DB']

# # Celery Configuration docker
CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']

django_heroku.settings(locals(), test_runner=False)