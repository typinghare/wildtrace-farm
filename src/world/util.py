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
    a = image.get_alpha()
    cropped_image = image.subsurface(rect)

    # Set alpha channel for the cropped image
    cropped_image.set_alpha(255)

    return cropped_image


def scale_image(image: pygame.Surface, scale_factor: int) -> pygame.Surface:
    """
    Scales a Pygame surface by a specified factor.
    :param image: The Pygame surface to be scaled.
    :param scale_factor: The factor by which the image should be scaled.
    :return: A new Pygame surface representing the scaled image.
    """
    new_size = (image.get_width() * scale_factor, image.get_height() * scale_factor)

    image = pygame.transform.scale(image, new_size)
    image.set_alpha(255)

    return image
