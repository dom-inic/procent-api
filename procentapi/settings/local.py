# for local use development
import os
from procentapi.settings.base import BASE_DIR
from . base import *


DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
REDIS_DB = 1