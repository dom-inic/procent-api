# for local use development
import os
from procentapi.settings.base import BASE_DIR
from . base import *


DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

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

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
REDIS_DB = 1