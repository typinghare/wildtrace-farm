"""
Game module.
"""

import pygame

from src.core.animation import AnimationManager
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
        self.settings: Settings = Settings()

        # Game context; this context is throughout the entire game life cycle
        self.context: Context = Context(self)

        # Initialize an event manager
        self.event_manager: EventManager = self.initEventManager()

        # Main display
        self.display: Display = Display(
            self.settings.display_cell_size,
            self.settings.display_grid_size,
            self.settings.display_scale_factor,
        )

        # Animation manager
        self.animation_manager: AnimationManager = AnimationManager(self.settings.fps)

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
            clock.tick(self.settings.fps)

    def trigger_events(self):
        """
        Gets all events from the event queue, and trigger the events one by one.
        """
        for event in pygame.event.get():
            self.event_manager.trigger(event, self.context)

    # @staticmethod
    def initEventManager(self) -> EventManager:
        """
        Initializes and returns a event manager.
        """
        event_manager = EventManager()

        # Quit the game
        def quit_game():
            self.context.running = False

        event_manager.on(pygame.QUIT, quit_game)

        # Update animation frame
        def update_animation_frame():
            self.animation_manager.update_frame()

        event_manager.on(EventTypes.BEFORE_RENDER, update_animation_frame)

        return event_manager
