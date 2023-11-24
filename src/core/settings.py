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

            # [Display] Window caption
            self.display_window_caption = "Wildtrace Farm"

            # [Display] Window size
            self.display_window_size = Size(1280, 800)

            # [Display] Default display background
            self.background = "#333333"

            # [Display] cell size; how many pixels does a cell contain
            self.display_cell_size = Size(32, 32)

            # [Display] scale factor
            self.display_scale_factor = 2

            # [Character] animation fps
            self.character_animation_fps = 8

            # [Character] size
            self.character_size = Size(96, 96)

        return cls._instance
