# pull official base image and configure the Docker file to use multi-stage build
FROM python:3.10-alpine AS build-python
RUN apk update && apk add --virtual build-essential gcc python3-dev musl-dev postgresql-dev
RUN python -m venv /opt/venv

# set environment variables
ENV PATH="/opt/venv/bin:$PATH"
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2 for database management
RUN pip install psycopg2-binary

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# set work directory
WORKDIR /app

# copy project
COPY . .

# collect static files (with whitenoise)
RUN python manage.py collectstatic --noinput

# add and run as non-root user (recommended by Heroku)
RUN adduser -D myuser
USER myuser

CMD gunicorn carbon.wsgi:application --bind 0.0.0.0:$PORT