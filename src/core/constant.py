"""
Core constants.
"""

import pygame


class EventTypes:
    """
    Custom event types.
    """

    BASE = pygame.USEREVENT

    # on-start event
    ON_START = BASE + 1

    # Before-render event
    BEFORE_RENDER = BASE + 2

    # After-render event
    AFTER_RENDER = BASE + 3
