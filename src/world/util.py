"""
Utility module.
"""

from typing import Tuple

import pygame


def crop_image(
    image: pygame.Surface, pos: Tuple[int, int], size: Tuple[int, int]
) -> pygame.Surface:
    """
    Crops an image and returns a sub-image.
    :param image: The image to crop from.
    :param pos: The position of the sub-image in the original image.
    :param size: The size of the sub-image.
    :return: The image being cropped.
    """
    rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
    return image.subsurface(rect)


def scale_image(image: pygame.Surface, scale_factor: float) -> pygame.Surface:
    """
    Scales a Pygame surface by a specified factor.
    :param image: The Pygame surface to be scaled.
    :param scale_factor: The factor by which the image should be scaled.
    :return: A new Pygame surface representing the scaled image.
    """
    new_size = (image.get_width() * scale_factor, image.get_height() * scale_factor)
    return pygame.transform.scale(image, new_size)
