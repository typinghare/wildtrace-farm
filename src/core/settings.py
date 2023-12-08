"""
Settings module.
"""

import os

from src.core.common import Size


class Settings:
    """
    Game settings. It is a singleton class.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            self = cls._instance = super(Settings, cls).__new__(cls)

            # Assets directory (absolute path)
            self.assets_dir = os.path.abspath(os.path.join(__file__, "../../../assets"))

            # Frame per second
            self.fps = 60

            # Debug mode
            self.debug = False

            # [Display] Window caption
            self.display_window_caption = "Wildtrace Farm"

            # [Display] Window size
            self.display_window_size = Size(1200, 720)

            # [Display] Default display background
            self.background = "#333333"

            # [Display] tile scale factor
            self.display_tile_scale_factor = 3

            # [Display] character scale facter
            self.display_character_scale_factor = 2

            # [Display] cell size; how many pixels does a cell contain
            # Cell size: Size(48, 48)
            # Grid size: Size(25, 15)
            self.display_cell_size = Size(
                16 * self.display_tile_scale_factor, 16 * self.display_tile_scale_factor
            )

            # [Character] animation fps
            self.character_animation_fps = 10

            # [Character] size
            self.character_size = Size(
                48 * self.display_character_scale_factor, 48 * self.display_character_scale_factor
            )

            # [Message box] font
            self.message_box_font = "manaspace/manaspc.ttf"

            # [Inventory]
            self.inventory_background_color = "#c38e70"
            self.inventory_slot_background_color = "#f3d5b5"
            self.inventory_selected_slot_background_color = "#ffee99"

            # [Sleep]
            self.sleep_fade_speed = 25

        return cls._instance
