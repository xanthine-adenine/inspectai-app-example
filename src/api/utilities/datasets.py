from typing import Any

from inspect_ai.dataset import Dataset, hf_dataset


class DatasetBase:
    """A dataset implementation base, with methods to download and process data."""

    def __init__(self, dataset_name: str, cached_file_name: str):
        self.__dataset_name = dataset_name
        self.__cached_file_name = cached_file_name

    def load_dataset(self, **kwargs) -> Dataset:
        raise NotImplementedError("not implemented")

    @property
    def dataset_name(self) -> str:
        return self.__dataset_name

    @property
    def cached_file_name(self) -> str:
        return self.__cached_file_name


class WinoGrandeDataset(DatasetBase):
    """WinoGrandeDataset."""

    def __init__(self):
        super().__init__("WinoGrande", "winogrande_dataset.json")

    def load_dataset(self) -> Dataset:
        dataset = hf_dataset("allenai/winogrande", "test")
        return dataset

datasets = [WinoGrandeDataset()]
datasets_by_name = {ds.dataset_name:ds for ds in datasets}
