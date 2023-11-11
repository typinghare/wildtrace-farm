"""
Game context module.
"""

from typing import Dict

from .settings import Settings


class Context:
    """
    Game Context.
    """

    def __init__(self, game):
        # Game
        self.game = game

        # Game settings
        self.settings: Settings = game.settings

        # Whether the game is running
        self.running: bool = True

        # Extra context data store
        self.data: Dict[str, object] = {}

    def set(self, key: str, value: object):
        """
        Set a value associated with a given key in the extra data store.
        :param key: The key for the data.
        :param value: The value to be stored.
        :return: The value.
        """
        self.data[key] = value

        return value

    def get(self, key: str):
        """
        Retrieve the value associated with a given key in the extra data store.
        :param key: The key for the data.
        :return: The value associated with the given key; None if the key is not found.
        """
        return self.data[key]
