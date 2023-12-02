"""
Inventory module.
"""
from pygame import Vector2, Rect, Surface

from src.core.common import Size
from src.core.context import Context
from src.core.display import Layer
from src.world.item.chest import Chest
from src.world.util import get_font


class Inventory:
    """
    Inventory
    """

    def __init__(self, context: Context):
        # Game context
        self.context: Context = context

        # Cell size
        self.cell_size: Size = context.settings.display_cell_size

        # Slot frame border
        self.frame_border = 6

        # Layer
        self.layer: Layer = Layer(Size(900, 250))

        # Chest
        self.chest: Chest | None = None

        # Whether the is displayed
        self.displayed = False

        # Init
        self._init_layer()

    def _init_layer(self) -> None:
        """
        Initializes the layer.
        """
        self.context.display.set_layer("inventory", self.layer)
        self.layer.offset = Vector2(100, 100)
        self.layer.hidden = True

    def update(self) -> None:
        """
        Updates the layer.
        """
        self.layer.hidden = not self.displayed
        if self.layer.hidden or self.chest is None:
            return

        num_col = self.chest.size.width
        num_row = self.chest.size.height
        cell_width = self.cell_size.width
        cell_height = self.cell_size.height
        border = self.frame_border
        slot_color = self.context.settings.inventory_slot_background_color
        selected_slot_color = self.context.settings.inventory_selected_slot_background_color
        selected_index: int = self.chest.get_selected_index()

        for row in range(num_row):
            for col in range(num_col):
                dest = Rect(
                    border * (col + 1) + cell_width * col,
                    border * (row + 1) + cell_height * row,
                    cell_width,
                    cell_height,
                )

                index = row * num_col + col
                color = selected_slot_color if selected_index == index else slot_color
                self.layer.surface.fill(color, dest)

                item = self.chest.get_item(index)
                if item is None:
                    continue

                self.layer.surface.blit(item.image, dest)

    def open_chest(self, chest: Chest) -> None:
        """
        Opens a chest and displays the inventory panel.
        """
        self.chest = chest
        self.displayed = True

        # Create a new surface
        num_col = self.chest.size.width
        num_row = self.chest.size.height
        cell_width = self.cell_size.width
        cell_height = self.cell_size.height
        border = self.frame_border
        self.layer.surface = Surface(
            (
                self.frame_border * (num_col + 1) + cell_width * num_col,
                self.frame_border * (num_row + 1) + cell_height * num_row + 75,
            )
        )

        # Background color
        background_color = self.context.settings.inventory_background_color
        self.layer.surface.fill(background_color)

        screen_size = self.context.display.size
        self.layer.offset = Vector2(
            (screen_size.width - self.layer.surface.get_width()) // 2,
            (screen_size.height - self.layer.surface.get_height()) // 2,
        )

        # Illustrations
        font = get_font(18, "manaspace/manaspc.ttf")
        illustrations = [
            "Press [C] to close the chest.",
            "Press [N] to move an item to the chest.",
            "Press [M] to move an item to the hotbar.",
        ]
        for line_index, illustration in enumerate(illustrations):
            text_surface = font.render(illustration, False, "black")
            y = (border + 1) * num_row + num_row * cell_height + line_index * 25 + 5
            self.layer.surface.blit(text_surface, Vector2(border * 2, y))

    def close_chest(self) -> None:
        """
        Closes the chest
        """
        self.chest = None
        self.displayed = False
