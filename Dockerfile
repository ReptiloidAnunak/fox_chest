FROM python:3.10-slim

WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . .

# Собираем статические файлы
RUN python ./manage.py collectstatic --noinput

# Запускаем Gunicorn
CMD gunicorn fox_shop.wsgi:application -b 0.0.0.0:8000
#
#CMD python manage.py runserver 0.0.0.0:8000

