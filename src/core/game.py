"""
Game module.
"""
import pygame

from .display import Display
from .event import EventManager
from .loop import LoopManager
from .settings import Settings
from .context import Context
from .constant import EventTypes
from src.world.data.registries import Registries


class Game:
    """
    Game.
    """

    def __init__(self):
        # Game settings
        self.settings: Settings = Settings()

        # Game context
        self.context: Context = Context(self)

        # Game event manager
        self.event_manager: EventManager = EventManager()

        # Game display
        self.display: Display = Display(self.settings.display_window_size, self.settings.background)

        # Game loop manager
        self.loop_manager: LoopManager = LoopManager()

        # Whether the game is running
        self.running: bool = True

    def init(self):
        """
        Initializes the game.
        """
        # Pygame initialization
        pygame.init()

        # Window
        pygame.display.set_caption(self.settings.display_window_caption)

        # Register all events to event manager
        for ref in Registries.EventListener.get_ref_list():
            event_listener = ref.res
            self.event_manager.register(event_listener)

        # Triggers on-start events
        self.event_manager.trigger(EventManager.create_event(EventTypes.ON_START), self.context)

        # white
        self.display.screen.fill("white")

    def run(self):
        """
        Starts the game loop. The game loop will never stop until users quit this game.
        """
        clock = pygame.time.Clock()
        while self.running:
            EventManager.post(EventTypes.BEFORE_RENDER)
            self.event_manager.trigger_all(self.context)

            self.display.render()
            self.display.flip()

            after_render_event = EventManager.create_event(EventTypes.AFTER_RENDER)
            self.event_manager.trigger(after_render_event, self.context)

            self.context.dt = round(clock.tick(self.settings.fps))
