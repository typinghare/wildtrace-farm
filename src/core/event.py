"""
Event module.
"""
from typing import Dict, List, Callable
import inspect

from pygame.event import Event

from .context import Context


class EventListener:
    """
    Game event listener.
    """

    def __init__(self, event_type: int, callback: Callable[[Context], None] | Callable[[], None]):
        # The type of event to listen for
        self.event_type: int = event_type

        # The callback to fire when the event is triggered
        self.callback: Callable[[Context], None] | Callable[[], None] = callback

    def invoke(self, context: Context):
        """
        Invokes the callback function.
        :param context: The game context.
        """
        num_args = len(inspect.signature(self.callback).parameters)
        if num_args == 0:
            self.callback()
        elif num_args == 1:
            self.callback(context)


class EventManager:
    """
    Game event manager.
    """

    def __init__(self):
        # Mapping from event types to lists of event listeners
        self._event_listener_map: Dict[int, List[EventListener]] = {}

    def trigger(self, event: Event | int, context: Context):
        """
        Trigger an event.
        :param event: The event (or event type) to trigger.
        :param context: The game context.
        """
        event_type: int = event if isinstance(event, int) else event.type
        event_listener_list = self._event_listener_map.get(event_type)
        if event_listener_list is not None:
            for event_listener in event_listener_list:
                event_listener.invoke(context)

    def register(self, event_listener: EventListener):
        """
        Registers an event listener.
        :param event_listener: The event listener to register.
        """
        event_type = event_listener.event_type
        callback = event_listener.callback
        self.on(event_type, callback)

    def on(self, event_type: int, callback: Callable[[Context], None]):
        """
        Listen for an event.
        :param event_type: The type of event to listen for.
        :param callback: The callback to fire when the event is triggered.
        :return:
        """
        if event_type not in self._event_listener_map:
            self._event_listener_map[event_type] = []

        self._event_listener_map[event_type].append(EventListener(event_type, callback))
