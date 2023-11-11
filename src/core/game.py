"""
Game module.
"""

import pygame

from src.core.settings import Settings
from src.core.context import Context
from src.core.event import EventManager
from src.core.display import Display
from src.core.event_types import EventTypes
from src.world.data.registries import Registries


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

        # Set the screen background color
        self.display.screen.fill("white")

        # Load and register all event listeners
        event_listener_ref_list = Registries.EventListener.get_ref_list()
        for event_listener_ref in event_listener_ref_list:
            event_listener = event_listener_ref.res
            self.event_manager.register(event_listener)

    def start(self):
        clock = pygame.time.Clock()

        # Post an on-start event
        pygame.event.post(pygame.event.Event(EventTypes.ON_START))
        self.trigger_events()

        while self.context.running:
            # Post a before-render event
            pygame.event.post(pygame.event.Event(EventTypes.BEFORE_RENDER))
            self.trigger_events()

            # Render the display
            self.display.render()

            # Post an after-render event
            pygame.event.post(pygame.event.Event(EventTypes.AFTER_RENDER))
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
