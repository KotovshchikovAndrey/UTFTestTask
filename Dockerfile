FROM python:3.12

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

COPY ./food_project ./

EXPOSE 8000