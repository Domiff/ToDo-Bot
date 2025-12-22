FROM python:3.13-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /backend

COPY ../pyproject.toml ./

ENV UV_PROJECT_ENVIRONMENT=/usr/local
RUN uv sync --group backend

COPY backend .

CMD ["gunicorn", "todo_manager.wsgi:application", "--bind", "0.0.0.0:8000"]
