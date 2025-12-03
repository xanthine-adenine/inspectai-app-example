FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /usr/local/app

RUN adduser --disabled-password app && chown -R app:app /usr/local/app

COPY pyproject.toml uv.lock .

RUN uv sync --frozen --no-dev

COPY src/ui ./ui

USER app

# Run streamlit server
CMD ["uv", "run", "streamlit", "run", "ui/app.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
