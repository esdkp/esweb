FROM python:3.8-slim-buster

ARG BUILD_COMMIT_SHA
ENV BUILD_COMMIT_SHA ${BUILD_COMMIT_SHA:-}

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /code
WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--access-logfile", "-", "esweb.wsgi:application"]
