FROM python:3.7-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /mikou_test


COPY manage.py requirements.txt /mikou_test/

RUN pip install -r requirements.txt && \
        python manage.py collectstatic --noinput
RUN python manage.py migrate
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
