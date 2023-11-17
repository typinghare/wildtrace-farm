"""
Window events.
"""

from src.core.context import Context


def quit_game(context: Context) -> None:
    """
    Quits the game.
    """
    context.game.running = False


def update_loops(context: Context) -> None:
    """
    Updates loops.
    """
    context.game.loop_manager.update(context.dt)
