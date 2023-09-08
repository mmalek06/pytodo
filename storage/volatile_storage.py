from storage.base_storage import BaseStorage


class VolatileStorage(BaseStorage):
    def __init__(self):
        self._storage = {}

    def add_item(self, item: any) -> int:
        next_index = len(self._storage)

        self._storage[next_index] = item

        return next_index

    def remove_item(self, index: int) -> None:
        del self._storage[index]

        sorted_values = [self._storage[key] for key in sorted(self._storage.keys())]
        new_storage = {}

        for idx in range(len(sorted_values)):
            new_storage[idx] = sorted_values[idx]

        self._storage = new_storage

    @property
    def items(self) -> dict[int, any]:
        return self._storage.copy()
