#######################################
#             BUILDER                 #
#######################################

FROM python:3.12.8-alpine AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code

RUN uv python pin 3.12.8

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-group dev

#######################################
#             RUNTIME                 #
#######################################

FROM python:3.12.8-alpine

ENV PATH="/code/.venv/bin:$PATH"

WORKDIR /code

COPY main.py /code/main.py

COPY src /code/src

COPY --from=builder /code/.venv /code/.venv

ENTRYPOINT ["python", "main.py"]
