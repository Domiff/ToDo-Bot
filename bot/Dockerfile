FROM python:3.13-slim-trixie AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /bot

COPY ../pyproject.toml ./

ENV UV_PROJECT_ENVIRONMENT=/usr/local
RUN uv sync --group bot


FROM python:3.13-slim-trixie

WORKDIR /bot

COPY  --from=builder /bot /bot

CMD ["python", "-m", "bot.main"]
