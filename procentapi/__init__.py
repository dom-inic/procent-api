# import celery to have it loaded when django starts
from .celery import app as celery_app