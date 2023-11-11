"""
Game settings module.
"""
from os import path


class Settings:
    """
    Game settings (singleton).
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)

            self = cls._instance

            # Assets directory (absolute path)
            self.assets_dir = path.abspath(path.join(__file__, "../../../assets"))

            # Framerate refers to the number of times the entire screen is redrawn
            # FPS = frame per second
            self.fps = 10

            # [Display] cell size
            self.display_cell_size = (16, 16)

            # [Display] grid size
            self.display_grid_size = (32, 24)

            # [Display] scale factor
            self.display_scale_factor = 2

        return cls._instance