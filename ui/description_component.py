from constants.command_constants import CommandConstants
from ui.base_component import BaseComponent


class DescriptionComponent(BaseComponent):
    def __init__(self):
        self._lines = [
            '',
            'This application is a TODO list.',
            'Use the below options to modify the list:',
            f'1. type \'{CommandConstants.ADD_COMMAND.value}\' and then type the TODO to be put on the list',
            f'2. type \'{CommandConstants.DEL_COMMAND.value}\' and choose element number to delete the item',
            f'3. type \'{CommandConstants.EXIT_COMMAND.value}\' to terminate the program'
        ]

    def draw(self) -> None:
        for line in self._lines:
            print(line)
