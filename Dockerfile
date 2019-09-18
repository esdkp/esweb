FROM python:3.7-slim

ARG BUILD_COMMIT_SHA
ENV BUILD_COMMIT_SHA ${BUILD_COMMIT_SHA:-}

ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image
COPY . /code
WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]

# Runs the production server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--access-logfile", "-", "esweb.wsgi:application"]
