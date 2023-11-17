"""
Settings module.
"""

import os

from src.core import Size


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

            # [Display] cell size; how many pixels does a cell contain
            self.display_cell_size = Size(16, 16)

            # [Display] scale factor
            self.display_scale_factor = 2

            # [Character] fps
            self.character_fps = 8

            # [Character] size
            self.character_size = Size(96, 96)

        return cls._instance
