FROM python:3.11 as builder

RUN apt-get install -y --no-install-recommends default-libmysqlclient-dev

ENV PATH=/root/.local/bin:$PATH

COPY ./requirements.txt /requirements.txt
RUN pip install --user -r /requirements.txt



FROM python:3.11-slim-buster

ARG BUILD_COMMIT_SHA
ENV BUILD_COMMIT_SHA ${BUILD_COMMIT_SHA:-}

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . /code
WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--access-logfile", "-", "esweb.wsgi:application"]
