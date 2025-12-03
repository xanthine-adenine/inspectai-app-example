from pathlib import Path

from fastapi import FastAPI

from .settings import settings


app = FastAPI(
    title="Inspect AI App Example",
    description="A simple example of building an app that uses the Inspect framework",
    version="0.1.0",
)


@app.get("/available_datasets")
async def available_datasets() -> dict[str, list[str]]:
    """Get the list of implemented datasets that can be used."""
    return {"datasets": []}


@app.get("/is_dataset_cached")
async def is_dataset_cached(file_name: str) -> dict[str, bool]:
    """Check if a dataset file exists in the data volume."""
    file_path = Path(settings.data_volume_path) / file_name
    return {"cached": file_path.exists()}
