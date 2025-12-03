.PHONY: help lint lint-fix build-api build-ui build-all start-dev stop-dev start stop clean

help:
	@echo "Available targets:"
	@echo "  lint            - Run ruff linter"
	@echo "  lint-fix        - Run ruff linter with auto-fix"
	@echo "  build-api       - Build API Docker image"
	@echo "  build-ui        - Build UI Docker image"
	@echo "  build-all       - Build both API and UI Docker images"
	@echo "  start-dev       - Start dev services with docker compose"
	@echo "  stop-dev        - Stop dev services with docker compose"
	@echo "  start           - Start services with docker compose"
	@echo "  stop            - Stop services with docker compose"
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

start-dev:
	docker compose -f docker-compose-dev.yaml up -d

stop-dev:
	docker compose -f docker-compose-dev.yaml down

start:
	docker compose -f docker-compose.yaml up -d

stop:
	docker compose -f docker-compose.yaml down

clean:
	docker rmi -f inspectai-app-api inspectai-app-ui || true
