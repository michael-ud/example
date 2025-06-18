FROM python:3.13.5-slim

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN apt-get update && apt-get -y install curl python3-dev
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /project

COPY ./pyproject.toml ./uv.lock ./

ENV PATH="$PATH:/root/.local/bin"

RUN uv venv ./.venv

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

WORKDIR /project/grocer
COPY grocer .

WORKDIR /project/cafe
COPY cafe .

WORKDIR /project

CMD . .venv/bin/activate && uvicorn cafe.main:app --host 0.0.0.0 --port 8081 --reload --reload-dir=/project/grocer --reload-dir=/project/cafe
