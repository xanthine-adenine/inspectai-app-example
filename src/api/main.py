from pathlib import Path

from fastapi import FastAPI, HTTPException

from .settings import settings
from .utilities.datasets import datasets_by_name


app = FastAPI(
    title="Inspect AI App Example",
    description="A simple example of building an app that uses the Inspect framework",
    version="0.1.0",
)


@app.get("/available_datasets")
async def available_datasets() -> dict[str, list[str]]:
    """Get the list of implemented datasets that can be used."""
    return {"datasets": sorted(datasets_by_name.keys())}


@app.get("/is_dataset_loaded")
async def is_dataset_loaded(dataset_name: str) -> dict[str, bool]:
    """Check if a dataset file exists in the data volume."""
    if dataset_name in datasets_by_name:
        file_name = datasets_by_name[dataset_name].cached_file_name
        file_path = Path(settings.data_volume_path) / file_name
        return {"loaded": file_path.exists()}
    else:
        return {"loaded": False}

@app.post("/load_dataset")
async def load_dataset(dataset_name: str) -> None:
    """Load a dataset's data."""
    if dataset_name in datasets_by_name:
        ds = datasets_by_name[dataset_name].load_dataset()
    else:
        raise HTTPException(404)
