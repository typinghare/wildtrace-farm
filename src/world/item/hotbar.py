"""
Tool box module.
"""
from pygame import Vector2, font, Rect, Surface

from src.core.common import Size
from src.core.context import Context
from src.core.display import Layer
from src.world.item.chest import Chest
from src.world.util import get_font, get_outlined_text_surface


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

        # Slot frame border
        self.frame_border = 6

        # Layer
        self.size: Size = Size(
            (self.slot_size.width + self.frame_border) * self.slot_number + self.frame_border,
            self.slot_size.height + self.frame_border * 2,
        )
        self.layer: Layer = Layer(self.size)

        # Chest
        self.chest: Chest = Chest(Size(10, 1))

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

    def update(self) -> None:
        """
        Updates this tool box.
        """
        item_list = self.chest.item_list
        selected_item_index: int | None = self.chest.get_selected_index()
        self.layer.surface.fill(self.context.settings.inventory_background_color)
        number_text_font = font.Font(None, 16)
        stack_text_font = get_font(18)

        slot_color = self.context.settings.inventory_slot_background_color
        selected_slot_color = self.context.settings.inventory_selected_slot_background_color
        for index in range(self.slot_number):
            item = item_list[index]
            rect = Rect(
                self.frame_border + index * (self.slot_size.width + self.frame_border),
                self.frame_border,
                self.slot_size.width,
                self.slot_size.height,
            )

            # Fill white color / Blit image
            is_item_selected = index == selected_item_index
            background_color = selected_slot_color if is_item_selected else slot_color
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
                    stack_str = str(stack_number)
                    text_surface = get_outlined_text_surface(
                        stack_str,
                        stack_text_font,
                        "#333333",
                        "#FFFFFF",
                    )
                    stack_dest = (rect.right - 5 * (1 + len(stack_str)) - 3, rect.bottom - 16)
                    self.layer.surface.blit(text_surface, stack_dest)

            # Blit the number in the top-left corner
            number_text = number_text_font.render(str((index + 1) % 10), True, "#333333")
            number_dest = (rect.left + 3, rect.top + 3)
            self.layer.surface.blit(number_text, number_dest)
