FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

RUN pip3 install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false && poetry install
ADD . /app/

EXPOSE 80
