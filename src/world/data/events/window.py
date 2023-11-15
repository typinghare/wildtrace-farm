"""
Window events.
"""

from src.core.context import Context


def quit_game(context: Context):
    """
    Quits the game.
    """
    context.game.running = False
