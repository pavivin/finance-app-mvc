FROM python:3.10-slim

WORKDIR /app

RUN python3 -m pip install poetry

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .

CMD python app/main.py