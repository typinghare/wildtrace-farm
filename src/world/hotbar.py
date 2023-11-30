"""
Tool box module.
"""
from pygame import Vector2, font, Rect, Surface

from src.core.common import Size
from src.core.context import Context
from src.core.display import Layer
from src.world.item.chest import Chest


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
        self.layer.surface.fill("#c38e70")
        number_text_font = font.Font(None, 16)
        stack_text_font = font.Font(None, 20)

        for index in range(self.slot_number):
            item = item_list[index]
            rect = Rect(
                self.frame_thickness + index * (self.slot_size.width + self.frame_thickness),
                self.frame_thickness,
                self.slot_size.width,
                self.slot_size.height,
            )

            # Fill white color / Blit image
            is_item_selected = index == selected_item_index
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
                    stack_str = str(stack_number)
                    stack_text = stack_text_font.render(stack_str, True, "#999999")
                    stack_dest = (rect.right - 5 * (1 + len(stack_str)), rect.bottom - 12)
                    self.layer.surface.blit(stack_text, stack_dest)

            # Blit the number in the top-left corner
            number_text = number_text_font.render(str((index + 1) % 10), True, "#333333")
            number_dest = (rect.left + 3, rect.top + 3)
            self.layer.surface.blit(number_text, number_dest)
