"""
Layer events.
"""
from src.core.context import Context
from src.core.display import Layer


def init_layer(context: Context) -> None:
    """
    Initializes layers.
    """
    idle_layer = Layer(context.display.size)
    layer_name_list = [
        # map layers
        "water",
        "ground",
        "floor",
        "furniture_bottom",
        "furniture_top",
        # other
        "character",
        "tool",
        "message_box",
        "debug",
    ]

    for layer_name in layer_name_list:
        context.display.unshift_layer(layer_name, idle_layer)
