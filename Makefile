.PHONY: help lint lint-fix build-api build-ui build-all start stop clean

help:
	@echo "Available targets:"
	@echo "  lint            - Run ruff linter"
	@echo "  lint-fix        - Run ruff linter with auto-fix"
	@echo "  build-api       - Build API Docker image"
	@echo "  build-ui        - Build UI Docker image"
	@echo "  build-all       - Build both API and UI Docker images"
	@echo "  start           - Start services with docker-compose"
	@echo "  stop            - Stop services with docker-compose"
	@echo "  clean           - Remove Docker images"

lint:
	uv run ruff check .

lint-fix:
	uv run ruff check --fix .

build-api:
	docker build -f api.Dockerfile -t inspectai-app-api .

build-ui:
	docker build -f ui.Dockerfile -t inspectai-app-ui .

build-all: build-api build-ui

start:
	docker compose up -d

stop:
	docker compose down

clean:
	docker rmi -f inspectai-app-api inspectai-app-ui || true
