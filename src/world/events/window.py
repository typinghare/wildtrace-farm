"""
Window events.
"""
import pygame.display

from src.core.context import Context


def set_caption(context: Context) -> None:
    """
    Sets the window caption
    """
    pygame.display.set_caption(context.settings.display_window_caption)


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
