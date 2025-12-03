"""Functions for calling the backend API."""

import logging

import httpx

from settings import settings

logger = logging.getLogger(__name__)


def available_datasets() -> list[str]:
    """Get the list of implemented datasets."""
    url = f"{settings.api_url}/available_datasets"
    try:
        response = httpx.get(url)
        return response.json().get("datasets", [])
    except Exception as e:
        logger.error(f"Error checking available datasets: {e}", exc_info=True)
        return []


def is_dataset_loaded(dataset_name: str) -> str:
    """Check if dataset has been cached locally or needs to be pulled."""
    url = f"{settings.api_url}/is_dataset_loaded"
    try:
        response = httpx.get(url, params={"dataset_name": dataset_name})
        return str(response.json().get("loaded", "unknown")).lower()
    except Exception as e:
        logger.error(f"Error checking dataset cache for '{dataset_name}': {e}", exc_info=True)
        return "error"


def load_dataset(dataset_name: str) -> None:
    url = f"{settings.api_url}/load_dataset"
    try:
        _ = httpx.post(url, params={"dataset_name": dataset_name})
    except Exception as e:
        logger.error(f"Error loading dataset'{dataset_name}': {e}", exc_info=True)
