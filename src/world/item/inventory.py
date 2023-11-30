"""
Inventory module.
"""
from pygame import Vector2

from src.core.common import Size
from src.core.context import Context
from src.core.display import Layer
from src.world.item.chest import Chest


class Inventory:
    """
    Inventory
    """

    def __init__(self, context: Context):
        # Game context
        self.context: Context = context

        # Cell size
        self.cell_size: Size = context.settings.display_cell_size

        # Layer
        self.layer: Layer = Layer(Size(900, 1000))

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
        self.layer.hidden = self.displayed
        if self.layer.hidden:
            return

    def open_chest(self, chest: Chest) -> None:
        """
        Opens a chest and displays the inventory panel.
        """
        self.chest = chest
        self.displayed = True

    def close_chest(self) -> None:
        """
        Closes the chest
        """
        self.chest = None
        self.displayed = False
