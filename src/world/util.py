"""
Utility module.
"""
import os
from typing import Tuple, Dict

from pygame import Surface, Rect, transform, font, mixer

from src.core.settings import Settings


def crop_image(image: Surface, pos: Tuple[int, int], size: Tuple[int, int]) -> Surface:
    """
    Crops an image and returns a sub-image.
    :param image: The image to crop from.
    :param pos: The position of the sub-image in the original image.
    :param size: The size of the sub-image.
    :return: The image being cropped.
    """
    rect = Rect(pos[0], pos[1], size[0], size[1])
    return image.subsurface(rect)


def scale_image(image: Surface, scale_factor: float) -> Surface:
    """
    Scales a Pygame surface by a specified factor.
    :param image: The Pygame surface to be scaled.
    :param scale_factor: The factor by which the image should be scaled.
    :return: A new Pygame surface representing the scaled image.
    """
    new_size = (image.get_width() * scale_factor, image.get_height() * scale_factor)
    return transform.scale(image, new_size)


font_instance_memo: Dict[Tuple[int, str], font.Font] = {}
assets_dir: str = Settings().assets_dir


def get_font(size: int, file: str | None = None) -> font.Font:
    """
    Gets a font.
    :param size The size of the font.
    :param file: The path of the font file.
    """
    key = (size, file)
    if key in font_instance_memo:
        return font_instance_memo[key]

    if file is not None:
        file = os.path.abspath(os.path.join(assets_dir, "fonts/", file))

    font_instance = font.Font(file, size)
    font_instance_memo[key] = font_instance

    return font_instance


def play_music(music_path: str) -> None:
    """
    Play a specific piece of music.
    """
    mixer.music.load(music_path)
    mixer.music.play(-1)


def stop_music() -> None:
    """
    Stop playing the music.
    """
    mixer.music.stop()
