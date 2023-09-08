from storage.base_storage import BaseStorage
from ui.base_component import BaseComponent


class ListComponent(BaseComponent):
    def __init__(self, storage: BaseStorage, width: int = 30):
        self._storage = storage
        self._width = width
        self._horizontal_border = '#' * width
        self._vertical_border = '#'

    def draw(self) -> None:
        print(self._horizontal_border)

        empty_line = self._get_empty_line()

        print(empty_line)
        self._draw_items()
        print(empty_line)
        print(self._horizontal_border)

    def _draw_items(self) -> None:
        items = self._storage.items
        sorted_values = [items[key] for key in sorted(items.keys())]
        # 2 for element number + 2 for borders + 2 for left and right spaces + 3 for ellipsis
        max_value_len = self._width - 2 - 2 - 2 - 3
        empty_line = self._get_empty_line()

        for idx in range(0, len(sorted_values)):
            value = sorted_values[idx]

            if len(value) > max_value_len:
                value = f'{value[:max_value_len - 3]}...'

            number = f' {idx + 1} '
            fill_size = len(empty_line) - len(value) - len(number) - 4
            fill = ' ' * fill_size
            line = f'{self._vertical_border}{number}{value} {fill} {self._vertical_border}'

            print(line)

    def _get_empty_line(self) -> str:
        return f'{self._vertical_border}{" " * (self._width - 2)}{self._vertical_border}'
