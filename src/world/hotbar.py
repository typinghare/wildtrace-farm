"""
Tool box module.
"""
from typing import List

from pygame import Vector2, font, Rect, Surface

from src.core.common import Size
from src.core.context import Context
from src.core.display import Layer
from src.world.item.item import GameItem, Item


class Hotbar:
    """
    Tool box.
    """

    def __init__(self, context: Context):
        # Game context
        self.context: Context = context

        # Number of slots
        self.slot_number = 10

        # Slot size
        cell_size = context.settings.display_cell_size
        self.slot_size = Size(cell_size.width, cell_size.height)

        # Slot frame thickness
        self.frame_thickness = 6

        # Layer
        self.size: Size = Size(
            (self.slot_size.width + self.frame_thickness) * self.slot_number + self.frame_thickness,
            self.slot_size.height + self.frame_thickness * 2,
        )
        self.layer: Layer = Layer(self.size)

        # Item list
        self.item_list: List[GameItem | None] = [None] * self.slot_number

        # Selected item index
        self._selected_index: int = 0

        # Init
        self._init_layer()

    def _init_layer(self) -> None:
        """
        Initializes layer.
        """
        screen_size = self.context.display.size
        self.context.display.set_layer("hotbar", self.layer)
        self.layer.offset = Vector2(
            (screen_size.width - self.size.width) // 2,
            screen_size.height * 0.98 - self.size.height,
        )

        self.layer.surface.fill("#c38e70")

    def select_item(self, index: int):
        """
        Selects an item.
        :param index: The index of the item.
        """
        if 0 <= index < self.slot_number:
            self._selected_index = index

    def get_item(self, index: int) -> GameItem | None:
        """
        Returns a specified item.
        """
        return self.item_list[index]

    def get_selected_item(self) -> GameItem | None:
        """
        Returns the selected game item.
        """
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
        for index in range(self.slot_number):
            game_item = self.item_list[index]
            if game_item is not None and game_item.stack == 0:
                self.item_list[index] = None

    def update(self) -> None:
        """
        Updates this tool box.
        """
        self.layer.surface.fill("#c38e70")
        number_text_font = font.Font(None, 16)
        stack_text_font = font.Font(None, 20)

        for index in range(self.slot_number):
            item = self.item_list[index]
            rect = Rect(
                self.frame_thickness + index * (self.slot_size.width + self.frame_thickness),
                self.frame_thickness,
                self.slot_size.width,
                self.slot_size.height,
            )

            # Fill white color / Blit image
            is_item_selected = index == self._selected_index
            background_color = "#ffee99" if is_item_selected else "#f3d5b5"
            surface = Surface(self.slot_size.toTuple())
            surface.fill(background_color)
            if item is None:
                self.layer.surface.blit(surface, rect)
            else:
                surface.blit(item.image, (0, 0))
                self.layer.surface.blit(surface, rect)

                # Blit the stack number in the bottom-right corner
                stack_number = item.stack
                if stack_number > 1:
                    s = str(stack_number)
                    stack_text = stack_text_font.render(s, True, (255, 255, 255))
                    stack_dest = (rect.right - 5 * (1 + len(s)), rect.bottom - 12)
                    self.layer.surface.blit(stack_text, stack_dest)

            # Blit the number in the top-left corner
            number_text = number_text_font.render(str((index + 1) % 10), True, "#333333")
            number_dest = (rect.left + 3, rect.top + 3)
            self.layer.surface.blit(number_text, number_dest)
