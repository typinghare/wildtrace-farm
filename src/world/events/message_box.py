"""
Message box related functions.
"""

import pygame

from src.core.context import Context
from src.world.message_box import MessageBox


def init_message_box(context: Context) -> None:
    """
    Initializes message box.
    """
    message_box = context["message_box"] = MessageBox(context)

    # message_box.play("This is a test message.")


def update_message_box(context: Context) -> None:
    """
    Updates message box.
    """
    message_box: MessageBox = context["message_box"]
    message_box.update()


def message_box_key_down(context: Context) -> None:
    """
    Message box key down.
    """
    # When the player press <J> when the message box is playing, stop the playing.
    key = context.event_data["key"]
    message_box: MessageBox = context["message_box"]

    if key == pygame.K_j:
        if message_box.message is None:
            return

        # Here, message_box.loop != None indicates that a message is being played
        if message_box.loop is not None:
            message_box.stop_playing()
        else:
            message_box.hide()
