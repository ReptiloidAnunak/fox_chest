FROM python:3.10-slim

WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
CMD python manage.py runserver 0.0.0.0:8000