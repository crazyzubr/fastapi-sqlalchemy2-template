FROM python:3.11-slim-buster

RUN apt-get update -y
RUN apt-get install -y build-essential libpq-dev python3-dev

WORKDIR /srv/someapp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN rm -rf .venv
RUN python3 -m venv .venv
RUN make envup

CMD ["make", "db_migrate", "run"]
