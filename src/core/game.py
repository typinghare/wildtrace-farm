"""
Game module.
"""

import pygame

from .settings import Settings
from .context import Context
from .event import EventManager
from .display import Display
from src.world import Tiles


class Game:
    """
    Game.
    """

    def __init__(self):
        # Game settings
        self.settings = Settings()

        # Game context; this context is throughout the entire game life cycle
        self.context = Context(self)

        # Initialize an event manager
        self.event_manager = self._initEventManager()

        # Main display
        self.display = Display(
            self.settings.display_cell_size,
            self.settings.display_grid_size,
            self.settings.display_scale_factor,
        )

    def init(self):
        """
        Initializes this game.
        :return:
        """
        pygame.init()

        self.display.screen.fill("white")

    def start(self):
        clock = pygame.time.Clock()

        self.display.grid[2][1].set_image(Tiles.WheatSeed)
        self.display.grid[2][2].set_image(Tiles.WheatSeedling)
        self.display.grid[2][3].set_image(Tiles.WheatVegetative)
        self.display.grid[2][4].set_image(Tiles.WheatBudding)
        self.display.grid[2][5].set_image(Tiles.WheatRipening)
        self.display.grid[2][6].set_image(Tiles.WheatProduct)

        while self.context.running:
            # Post a before-render event
            pygame.event.post(pygame.event.Event(Events.BEFORE_RENDER))
            self.trigger_events()

            # Render the display
            self.display.render()

            # Post an after-render event
            pygame.event.post(pygame.event.Event(Events.AFTER_RENDER))
            self.trigger_events()

            # Clock ticking
            clock.tick(self.settings.refresh_rate)

    def trigger_events(self):
        """
        Gets all events from the event queue, and trigger the events one by one.
        """
        for event in pygame.event.get():
            self.event_manager.trigger(event, self.context)

    @staticmethod
    def _initEventManager() -> EventManager:
        """
        Initializes and returns a event manager.
        """
        event_manager = EventManager()

        event_manager.on(pygame.QUIT, lambda context: setattr(context, "running", False))

        return event_manager


class Events:
    """
    Custom event enumeration.
    """

    BASE = pygame.USEREVENT

    # Before-render event
    BEFORE_RENDER = BASE + 1

    # After-render event
    AFTER_RENDER = BASE + 2
