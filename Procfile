web: gunicorn procentapi.wsgii --log-file -
worker: celery -A procentapi worker -l info
release: python manage.py migrate