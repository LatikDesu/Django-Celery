# Django-Celery


docker run -d -p 6379:6379 redis

celery -A mysite worker -l info

celery -A mysite flower  --address=127.0.0.6 --port=5566
