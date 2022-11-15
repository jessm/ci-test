FROM python:3.10.7

EXPOSE 80

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py makemigrations \
    && python manage.py migrate \
    && gunicorn ulticlipper.wsgi -b 0.0.0.0:80
