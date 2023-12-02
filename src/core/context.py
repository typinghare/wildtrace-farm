"""
Game context module.
"""

from typing import Dict, TYPE_CHECKING, Any

if TYPE_CHECKING:
    from src.core.settings import Settings
    from src.core.game import Game
    from src.core.display import Display
    from src.core.event import EventManager
    from src.core.loop import LoopManager


class Context:
    """
    Game Context.
    """

    def __init__(self, game: "Game"):
        # Game
        self.game: "Game" = game

        # Delta time in milliseconds
        # (dt is short for delta time, which refers to the time of a single frame)
        self.dt: int = 0

        # Event data
        self.event_data: Dict[str, Any] = {}

        # Extra context data store
        self._data: Dict[str, object] = {}

    @property
    def settings(self) -> "Settings":
        """
        Returns the game settings.
        """
        return self.game.settings

    @property
    def event_manager(self) -> "EventManager":
        """
        Returns the event manager.
        """
        return self.game.event_manager

    @property
    def display(self) -> "Display":
        """
        Returns the game display.
        """
        return self.game.display

    @property
    def loop_manager(self) -> "LoopManager":
        """
        Returns the event manager.
        """
        return self.game.loop_manager

    def __getitem__(self, key) -> Any:
        """
        Retrieves the value associated with a given key in the extra data store.
        :param key: The key for the data.
        :return: The value associated with the given key; None if the key is not found.
        """
        return self._data.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        """
        Sets a value associated with a given key in the extra data store.
        :param key: The key for the data.
        :param value: The value to be stored.
        :return: The value.
        """
        self._data[key] = value

    def __delitem__(self, key: str) -> None:
        """
        Deletes a key in the extra data store.
        :param key: The key for the data to delete.
        """
        del self._data[key]

    def __contains__(self, key: str) -> bool:
        """
        Checks whether a key is in the extra data store.
        :param key: The key to check.
        """
        return key in self._data
