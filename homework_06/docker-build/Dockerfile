FROM python:3.11.8
WORKDIR /opt/app

RUN pip install --upgrade pip "poetry==1.8.2"
RUN poetry config virtualenvs.create false --local

COPY ./app/poetry.lock ./app/pyproject.toml ./

RUN poetry install

COPY ./docker-build/entrypoint.sh entrypoint.sh

COPY ./app/ .

RUN ls -la
RUN pwd