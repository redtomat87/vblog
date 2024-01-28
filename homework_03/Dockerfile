FROM python:3.10.12-buster

WORKDIR /app

RUN pip install "poetry==1.7.1"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY app ./

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000