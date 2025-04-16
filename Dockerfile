FROM python:3.12.8-alpine

RUN pip install --no-cache-dir uv

RUN uv python pin 3.12.8

WORKDIR /code

COPY pyproject.toml /code

RUN uv sync --no-group test

COPY main.py /code/main.py

COPY src /code/src

CMD ["uv", "run", "python", "main.py"]
