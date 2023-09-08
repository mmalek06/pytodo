import os

from ui.base_component import BaseComponent


class LayoutComponent(BaseComponent):
    def __init__(self, components: list[BaseComponent]):
        self._components = components

    def draw(self) -> None:
        os.system('cls')

        for component in self._components:
            component.draw()
