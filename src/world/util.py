"""
Utility module.
"""
import os
from random import random
from typing import Tuple, Dict

import pygame
import numpy as np
from pygame import Surface, Rect, transform, font, surfarray

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


def darken_surface(original_surface, factor) -> Surface:
    # Get the pixels as a 3D array
    pixel_array = surfarray.array3d(original_surface)

    # Apply darkening to the pixel array
    darkened_array = np.multiply(pixel_array, factor)
    np.clip(darkened_array, 0, 255, out=darkened_array)

    # Create a new surface and update it with the modified pixel values
    darkened_surface = pygame.surfarray.make_surface(darkened_array)

    return darkened_surface


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


_circle_cache = {}


def _circle_points(r):
    r = int(round(r))
    if r in _circle_cache:
        return _circle_cache[r]
    x, y, e = r, 0, 1 - r
    _circle_cache[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points


def get_outlined_text_surface(
    text: str, _font: font.Font, inner_color: str, outer_color: str, opx=2
) -> Surface:
    text_surface = _font.render(text, True, inner_color).convert_alpha()
    w = text_surface.get_width() + 2 * opx
    h = _font.get_height()

    osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
    osurf.fill((0, 0, 0, 0))

    surf = osurf.copy()

    osurf.blit(_font.render(text, True, outer_color).convert_alpha(), (0, 0))

    for dx, dy in _circle_points(opx):
        surf.blit(osurf, (dx + opx, dy + opx))

    surf.blit(text_surface, (opx, opx))

    return surf


def flip_coin(true_possibility: float = 0.5) -> bool:
    """
    Returns a bool value.
    """

    return random() < true_possibility
