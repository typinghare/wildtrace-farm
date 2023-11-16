"""
Event module.
"""
from typing import Callable, Dict, List
import inspect

import pygame
from pygame.event import Event

from src.core.context import Context


class EventListener:
    """
    Event listener that responds to a specific type of event.
    """

    def __init__(self, event_type: int, callback: Callable[[Context], None] | Callable[[], None]):
        # The type of the event to listen for
        self.event_type: int = event_type

        # The callback function to invoke when the event occurs
        self._callback = callback

        # The number of parameters in the callback function
        self._callback_param_len = len(inspect.signature(callback).parameters)

        if self._callback_param_len > 1:
            raise Exception("The callback function should have either zero or one parameter.")

    def invoke(self, context: Context):
        """
        Invokes the callback function.
        :param context: The game context.
        """
        if self._callback_param_len == 0:
            self._callback()
        else:
            self._callback(context)


class EventManager:
    """
    An event manager serves as an observer that actively monitors all game events. Upon the
    occurrence of a game event, the corresponding callback functions within the registered event
    listeners are invoked.
    """

    def __init__(self):
        # A mapping from event types to lists of event listeners
        self._event_listener_map: Dict[int, List[EventListener]] = {}

    def register(self, event_listener: EventListener) -> EventListener:
        """
        Registers an event listener.
        :param event_listener: The event listener to register.
        :return The event listener registered.
        """
        event_type = event_listener.event_type

        if event_type not in self._event_listener_map:
            self._event_listener_map[event_type] = []

        self._event_listener_map[event_type].append(event_listener)

        return event_listener

    def on(self, event_type: int, callback: Callable[[Context], None]) -> EventListener:
        """
        Listens for an event.
        :param event_type: The type of the event to listen for.
        :param callback: The callback to fire when the event is triggered.
        :return The event listener registered.
        """
        return self.register(EventListener(event_type, callback))

    def trigger(self, event: Event, context: Context):
        """
        Triggers an event, invoking registered event listeners.
        :param event: The event to trigger.
        :param context: The game context.
        """
        event_listener_list = self._event_listener_map.get(event.type)

        if event_listener_list is not None:
            for event_listener in event_listener_list:
                context.event_data = event.dict
                event_listener.invoke(context)

    def trigger_all(self, context: Context):
        """
        Triggers all events in the Pygame buffer.
        :param context: The game context.
        """
        events = pygame.event.get()
        for event in events:
            self.trigger(event, context)

    @staticmethod
    def create_event(event_type: int, data: Dict | None = None) -> Event:
        """
        Creates a new event.
        :param event_type: The type of the event to post.
        :param data: Extra data associated with the event, if applicable.
        :return: The created event.
        """
        return (
            pygame.event.Event(event_type) if data is None else pygame.event.Event(event_type, data)
        )

    @staticmethod
    def post(event_type: int, data: Dict | None = None):
        """
        Posts an event to the Pygame event queue.
        :param event_type: The type of the event to post.
        :param data: Extra data associated with the event, if applicable.
        """
        event = (
            pygame.event.Event(event_type) if data is None else pygame.event.Event(event_type, data)
        )

        pygame.event.post(event)
