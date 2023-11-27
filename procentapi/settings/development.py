# deployed but still under development
# for local use development
import os
from procentapi.settings.base import BASE_DIR
from . base import *


DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'peaceful-badlands-38433-2cbf049590ab.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
        
    }
}

REDIS_HOST = 'ec2-44-196-160-1.compute-1.amazonaws.com'
REDIS_PORT = '16340'
REDIS_DB = 1

# Celery Configuration docker
CELERY_BROKER_URL = 'rediss://:p6da119e6d04a68daf6bfa00b216a2a45605feceee98f003355d56c3c9d177b0d@ec2-44-196-160-1.compute-1.amazonaws.com:16340'
