"""
Game context module.
"""

from typing import Dict, TYPE_CHECKING, Any

# An approach to circumvent the circular import error
if TYPE_CHECKING:
    from src.core.settings import Settings
    from src.core.game import Game


class Context:
    """
    Game Context.
    """

    def __init__(self, game: "Game"):
        # Game
        self.game: "Game" = game

        # Delta time in milliseconds
        # dt is short for delta time, which refers to the time of a single frame
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

    def set(self, key: str, value: Any) -> Any:
        """
        Sets a value associated with a given key in the extra data store.
        :param key: The key for the data.
        :param value: The value to be stored.
        :return: The value.
        """
        self._data[key] = value

        return value

    def get(self, key: str) -> Any:
        """
        Retrieves the value associated with a given key in the extra data store.
        :param key: The key for the data.
        :return: The value associated with the given key; None if the key is not found.
        """
        return self._data[key]
