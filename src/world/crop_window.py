"""
Crop window module.
"""
from pygame import Vector2, Surface

from src.core.common import Size
from src.core.context import Context
from src.core.display import Layer
from src.world.item.crop import GameCrop
from src.world.util import get_font


class CropWindow:
    """
    The window of the crop.
    """

    def __init__(self, context: Context):
        # Game context
        self.context: Context = context

        # Layer
        self.layer: Layer = Layer(Size(175, 100))

        # Alpha value
        self.alpha: int = 200

        # Init
        self._init_layer()

    def _init_layer(self) -> None:
        """
        Initializes layer.
        """
        # Align to bottom-left
        screen_size = self.context.display.size
        self.layer.offset = Vector2(0, screen_size.height - 200)
        self.context.display.set_layer("crop_window", self.layer)

        # Fill color (white, translucent)
        self.layer.surface.fill("white")
        self.layer.surface.set_alpha(self.alpha)

        # By default, it is hidden
        self.layer.hidden = True

    def reset_layer(self) -> None:
        """
        Resets the layer.
        """
        self.layer.surface = Surface(self.layer.size.toTuple())
        self.layer.surface.fill("white")
        self.layer.surface.set_alpha(self.alpha)

    def display_crop_info(self, game_crop: GameCrop | None) -> None:
        """
        Displays the information of a game crop.
        :param game_crop: The game crop object to display.
        """
        self.layer.hidden = game_crop is None
        if self.layer.hidden:
            return

        self.reset_layer()
        font = get_font(24)

        def get_key_text(key: str) -> Surface:
            return font.render(key, False, "#4a4e69")

        def get_value_text(value: str, color: str) -> Surface:
            return font.render(value, False, color)

        # 1. Name
        product = game_crop.crop.product
        name = product.item.name
        self.layer.surface.blit(get_key_text("Name:"), Vector2(10, 10))
        self.layer.surface.blit(get_value_text(name, "#3a86ff"), Vector2(75, 10))

        # 2. Stage string
        stage_str = game_crop.stage_str
        self.layer.surface.blit(get_key_text("Stage:"), Vector2(10, 40))
        self.layer.surface.blit(get_value_text(stage_str, "#57cc99"), Vector2(75, 40))

        # 3. Whether the crop is watered
        is_watered_str = "Irrigated" if game_crop.watered else "Unirrigated"
        is_watered_color = "#27a300" if game_crop.watered else "#ff5400"
        self.layer.surface.blit(get_key_text("Status:"), Vector2(10, 70))
        self.layer.surface.blit(get_value_text(is_watered_str, is_watered_color), Vector2(75, 70))
