"""
Layer events.
"""
from src.core.context import Context
from src.core.display import Layer


def init_layer(context: Context) -> None:
    display = context.display

    display.unshift_layer("tool", Layer(display.size))
    display.unshift_layer("character", Layer(context.settings.character_size))
    display.unshift_layer("furniture_top", Layer(display.size))
    display.unshift_layer("furniture_bottom", Layer(display.size))
    display.unshift_layer("floor", Layer(display.size))
    display.unshift_layer("ground", Layer(display.size))
    display.unshift_layer("water", Layer(display.size))
