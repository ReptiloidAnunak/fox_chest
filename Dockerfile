FROM python:3.10-slim

WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod -R 777 /app/media
RUN chmod -R 777 /app/static
CMD python manage.py runserver 0.0.0.0:8000