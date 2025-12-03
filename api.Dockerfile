FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /usr/local/app

COPY pyproject.toml .

RUN uv sync --frozen --no-dev

COPY src/api ./api

RUN useradd app
USER app

# Run uvicorn server
CMD ["uv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]