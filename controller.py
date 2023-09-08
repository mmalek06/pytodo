from constants.command_constants import CommandConstants
from storage.base_storage import BaseStorage
from ui.base_component import BaseComponent


class Controller:
    def __init__(self, layout: BaseComponent, storage: BaseStorage):
        self._layout = layout
        self._storage = storage

    def loop(self) -> None:
        while True:
            self._layout.draw()

            command = input()

            match command:
                case CommandConstants.ADD_COMMAND.value:
                    self._handle_add()
                case CommandConstants.DEL_COMMAND.value:
                    self._handle_del()
                case CommandConstants.EXIT_COMMAND.value:
                    return

    def _handle_add(self) -> None:
        todo = input()

        self._storage.add_item(todo)

    def _handle_del(self) -> None:
        try:
            index = int(input()) - 1

            self._storage.remove_item(index)
        except:
            pass
