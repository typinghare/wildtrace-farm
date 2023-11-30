"""
Chest module.
"""
from typing import List

from src.core.common import Size
from src.world.item.item import GameItem, Item


class Chest:
    """
    Chest can be used to store items.
    """

    def __init__(self, size: Size):
        # Inventory size
        self.size: Size = size

        # Inventory item size
        self.item_size = self.size.width * self.size.height

        # Item list
        self.item_list: List[GameItem | None] = [None] * self.size.width * self.size.height

        # Selected item index
        self._selected_index: int | None = None

    def select_item(self, index: int):
        """
        Selects an item.
        :param index: The index of the item.
        """
        if 0 <= index < self.item_size:
            self._selected_index = index

    def get_item(self, index: int) -> GameItem | None:
        """
        Returns a specified item.
        """
        return self.item_list[index]

    def get_selected_index(self) -> int | None:
        return self._selected_index

    def get_selected_item(self) -> GameItem | None:
        """
        Returns the selected game item.
        """
        if self._selected_index is None:
            return None

        return self.get_item(self._selected_index)

    def add_item(self, item: Item, stack: int = 1) -> bool:
        """
        Adds an item to this hotbar.
        :param item: The item too add.
        :param stack: The stack number.
        :return: True if the item is successfully added; false otherwise.
        """
        first_empty_slot_index = self.item_list.index(None)
        if first_empty_slot_index == -1:
            return False

        game_item = GameItem(item)
        self.item_list[first_empty_slot_index] = game_item
        game_item.stack = stack

        return True

    def stack_item(self, item: Item, increment: int = 1) -> bool:
        """
        Stacks an item.
        :param item: The item to stack.
        :param increment: The number of items.
        """
        remaining_number = increment
        for game_item in self.item_list:
            if game_item is not None and game_item.item == item and not game_item.is_full():
                remaining_number = game_item.stack_to_full(remaining_number)

        if remaining_number > 0:
            return self.add_item(item, remaining_number)

        return True

    def consume_selected_item(self, volume: int = 1) -> bool:
        """
        Consumes selected item.
        :param volume: The number of items to consume.
        :return: True if the selected item can be consumed successfully.
        """
        game_item: GameItem | None = self.get_selected_item()
        if game_item is None:
            return False

        result = game_item.decrease_stack(volume)
        if result:
            self.refresh()

        return result

    def refresh(self) -> None:
        """
        Refreshes items.
        """
        for index in range(self.item_size):
            game_item = self.item_list[index]
            if game_item is not None and game_item.stack == 0:
                self.item_list[index] = None
