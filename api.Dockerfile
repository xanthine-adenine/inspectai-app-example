FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /usr/local/app

RUN adduser --disabled-password app && chown -R app:app /usr/local/app

COPY pyproject.toml uv.lock .

RUN uv sync --frozen --no-dev

COPY src/api ./api

USER app

# Run uvicorn server
CMD ["uv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]