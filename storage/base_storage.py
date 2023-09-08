class BaseStorage:
    def add_item(self, item: any) -> int:
        raise NotImplemented

    def remove_item(self, index: int) -> None:
        raise NotImplemented

    @property
    def items(self) -> dict[int, any]:
        raise NotImplemented
