import os
import json

from constants.config import FILE_STORAGE_PATH
from storage.base_storage import BaseStorage
from storage.volatile_storage import VolatileStorage


class OnDiskStorage(BaseStorage):
    def __init__(self):
        self._storage = VolatileStorage()

    def load_saved_data(self):
        if not os.path.exists(FILE_STORAGE_PATH):
            OnDiskStorage._write_file_using_data({})

        with open(FILE_STORAGE_PATH, 'r') as json_file:
            data = json.load(json_file)

            self._reset_storage(data)

    def add_item(self, item: any) -> int:
        current_items = self.items

        try:
            next_index = self._storage.add_item(item)

            # it's much more probable that writing a file will fail than a dict add will
            # therefore exception handling should focus on reverting the in-memory changes
            self._write_file(self.items)

            return next_index
        except:
            # simple in-mem storage reset
            self._reset_storage(current_items)

            raise

    def remove_item(self, index: int) -> None:
        self._storage.remove_item(index)
        self._write_file(self.items)

    def _reset_storage(self, items: dict[int, any]) -> None:
        sorted_values = OnDiskStorage._sort_values(items)

        for value in sorted_values:
            self._storage.add_item(value)

    @staticmethod
    def _sort_values(data: dict[int, any]) -> list[any]:
        return [data[key] for key in sorted(data.keys())]

    @staticmethod
    def _write_file(data=None) -> None:
        if data is None:
            data = {}

        OnDiskStorage._write_file_using_data(data)

    @staticmethod
    def _write_file_using_data(data: dict) -> None:
        with open(FILE_STORAGE_PATH, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @property
    def items(self) -> dict[int, any]:
        return self._storage.items
