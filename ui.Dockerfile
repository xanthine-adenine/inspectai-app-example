FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /usr/local/app

COPY pyproject.toml .

RUN uv sync --frozen --no-dev

COPY src/ui ./ui

RUN useradd app
USER app

# Run streamlit server
CMD ["uv", "run", "streamlit", "run", "ui/app.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
