"""
Layer events.
"""
from src.core.context import Context
from src.core.display import Layer


def init_layer(context: Context) -> None:
    """
    Initializes layers.
    """
    display = context.display
    layer_name_list = [
        # map layers
        "water",
        "ground",
        "floor",
        "crop",
        "furniture_bottom",
        "furniture_top",
        # fixed
        "character",
        "tool_box",
        "hotbar",
        "data_window",
        "crop_window",
        "inventory",
        "shopping",
        "curtain",
        "message_box",
        # animation
        "animation",
        # debug
        "debug",
    ]

    for layer_name in layer_name_list:
        display.append_layer(layer_name, Layer(display.size))
