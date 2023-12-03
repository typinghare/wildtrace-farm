"""
Music resource module.
"""
import os.path

from src.core.settings import Settings
from src.registry import RegistryUtil
from src.world.data.registries import Registries

assets_dir = Settings().assets_dir


def register(path: str) -> str:
    """
    Registers a music.
    :param path: The file path to the music file.
    :return The absolute path of the music file.
    """
    absolute_path = os.path.abspath(os.path.join(assets_dir, "music", path))
    return Registries.Music.register(RegistryUtil.createLoc(path), absolute_path)


class Music:
    """
    Music resources.
    """

    Home = register("music.mp3")
    Farm = register("farm.mp3")
